#if defined _DEBUG
#else
#define NDEBUG
#endif

#define WIN32_LEAN_AND_MEAN

#include <ntstatus.h>
#include <Windows.h>
#include <winternl.h>
#include <Shlwapi.h>
#include <iostream>
#include <string>
#include <fstream>
#include <cassert>
#include <cstdint>
#include <cstddef>
#include <type_traits>

#pragma comment(lib, "ntdll.lib")

EXTERN_C NTSYSAPI
NTSTATUS NTAPI NtWriteVirtualMemory(
	_In_		HANDLE	ProcessHandle,
	_In_		PVOID	BaseAddress,
	_In_		PVOID	Buffer,
	_In_		SIZE_T	NumberOfBytesToWrite,
	_Out_opt_	PSIZE_T	NumberOfBytesWritten
);

EXTERN_C NTSYSAPI
NTSTATUS NTAPI NtOpenProcess(
	_Out_		PHANDLE				ProcessHandle,
	_In_		ACCESS_MASK			DesiredAccess,
	_In_		POBJECT_ATTRIBUTES	ObjectAttributes,
	_In_opt_	CLIENT_ID* ClientId
);

namespace detail
{
	template <typename T, typename Enable = void>
	struct recursive_decay
	{
		using type = std::decay_t<T>;
	};

	template <typename T>
	struct recursive_decay<T, std::enable_if_t<std::is_pointer_v<T>>>
	{
		using type = std::add_pointer_t<typename recursive_decay<std::remove_pointer_t<T>>::type>;
	};

	template <typename T>
	using recursive_decay_t = typename recursive_decay<T>::type;
}

template <typename T>
auto offset_ptr(T ptr, const std::ptrdiff_t offset) -> detail::recursive_decay_t<T>
{
	auto address = (std::uintptr_t)(ptr) + offset;
	return (detail::recursive_decay_t<T>)(address);
}

auto file_exists(std::string dll_name) -> bool
{
	return std::ifstream(dll_name).good();
}

auto get_process_id(std::string process_name) -> HANDLE
{
	auto len = ULONG(0);
	NtQuerySystemInformation(SystemProcessInformation, nullptr, 0, &len);
	const auto buf = alloca(len);
	auto ret = NtQuerySystemInformation(SystemProcessInformation, buf, len, nullptr);

	assert(NT_SUCCESS(ret));

	if (!NT_SUCCESS(ret))
		return INVALID_HANDLE_VALUE;

	auto it = PSYSTEM_PROCESS_INFORMATION(buf);

	do
	{
		char image_name[MAX_PATH + 1];
		ANSI_STRING image_name_astr{ 0, sizeof(image_name), image_name };

		ret = RtlUnicodeStringToAnsiString(&image_name_astr, &it->ImageName, FALSE);
		assert(NT_SUCCESS(ret));

		image_name[image_name_astr.Length] = 0;

		for (auto& c : image_name)
			c = tolower(c);

		if (image_name == process_name)
			return it->UniqueProcessId;
	} while (it->NextEntryOffset && ((it = offset_ptr(it, it->NextEntryOffset))));

	return INVALID_HANDLE_VALUE;
}

auto open_process(HANDLE pid, HANDLE & handle) -> void
{
	CLIENT_ID client_id;
	client_id.UniqueProcess = pid;
	client_id.UniqueThread = nullptr;

	OBJECT_ATTRIBUTES attr;
	InitializeObjectAttributes(&attr, nullptr, FALSE, nullptr, nullptr);

	auto ret = NtOpenProcess(&handle, PROCESS_ALL_ACCESS, &attr, &client_id);
	assert(NT_SUCCESS(ret));
}

auto close_process(HANDLE process) -> void
{
	NtClose(process);
}

auto inject(HANDLE process, std::string dll) -> void
{
	char dll_name[MAX_PATH] = { 0 };
	GetFullPathNameA(dll.c_str(), MAX_PATH, dll_name, 0);

	auto allocated_memory = VirtualAllocEx(process, nullptr, sizeof(dll_name), MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE);

	auto ret = NtWriteVirtualMemory(process, allocated_memory, dll_name, sizeof(dll_name), nullptr);
	assert(NT_SUCCESS(ret));

	CreateRemoteThread(process, 0, 0, (LPTHREAD_START_ROUTINE)LoadLibrary, allocated_memory, 0, 0);
}

auto main() -> int
{
	std::cout << "LoadLibrary DLL Injector" << std::endl << std::endl;

	auto dll_name{ std::string("") };
	std::cout << "DLL Name: ";
	std::cin >> dll_name;

	if (!file_exists(dll_name))
	{
		std::cout << std::endl << "[ERROR] DLL not found." << std::endl;
		system("pause");
		return EXIT_FAILURE;
	}

	auto process_name{ std::string("") };
	std::cout << "Process Name: ";
	std::cin >> process_name;

	const auto pid{ get_process_id(process_name) };

	if (pid == INVALID_HANDLE_VALUE)
	{
		std::cout << std::endl << "[ERROR] Process not found." << std::endl;
		system("pause");
		return EXIT_FAILURE;
	}

	static auto process{ INVALID_HANDLE_VALUE };

	open_process(pid, process);
	inject(process, dll_name);
	close_process(process);
	Beep(330, 1000);

	return EXIT_SUCCESS;
}
