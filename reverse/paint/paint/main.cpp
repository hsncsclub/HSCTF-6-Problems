#include <windows.h>
#include <stdio.h>
#include <thread>
#include <stdexcept>
#include <string>

#include "xor.hpp"

DWORD WINAPI entry(LPVOID lpThreadParameter)
{
	try
	{
		char pszPath[MAX_PATH] = { NULL };
		GetModuleFileName(NULL, pszPath, MAX_PATH);

		if (strcmp(pszPath, "C:\\WINDOWS\\system32\\mspaint.exe") == 0)
		{
			MessageBoxA(NULL, XorStr("hsctf{havent_seen_windows_in_a_while}"), "Flag", NULL);
		}
	}
	catch (const std::runtime_error& err)
	{
		MessageBoxA(NULL, err.what(), "Error", NULL);

		std::this_thread::sleep_for(std::chrono::seconds(1));
	}

	std::this_thread::sleep_for(std::chrono::seconds(1));

	FreeLibraryAndExitThread(static_cast<HMODULE>(lpThreadParameter), EXIT_SUCCESS);
}

BOOL APIENTRY DllMain(_In_ HINSTANCE hinstDLL, _In_ DWORD fdwReason, _In_ LPVOID lpvReserved)
{
	if (fdwReason == DLL_PROCESS_ATTACH)
	{
		DisableThreadLibraryCalls(hinstDLL);

		if (auto handle = CreateThread(nullptr, NULL, entry, hinstDLL, NULL, nullptr))
		{
			CloseHandle(handle);
		}
	}

	return TRUE;
}