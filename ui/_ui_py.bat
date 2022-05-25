@echo off

for %%A IN (*.ui) DO (
	for /f "tokens=1* delims=()" %%B IN ("%%~nA") DO (
		pyuic5 -x "%%~B".ui -o "%%~B".py
	)
)
