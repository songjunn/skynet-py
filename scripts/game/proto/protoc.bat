@echo off

@set SRC_DIR=.

cd %SRC_DIR%

for /f "delims=" %%i in ('dir /b /a-h "*.proto"') do (call protoc.exe -I=./ --python_out=../message %%i)

@pause