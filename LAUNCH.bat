@echo off
title Engine ML Project (TensorFlow-FREE)
echo.
echo  =========================================================
echo   Engine ML Prediction System  ^|  TensorFlow-FREE Build
echo  =========================================================
echo.
echo  [1] Run Task 1  (Monte Carlo Simulation)
echo  [2] Run Task 2  (ML Model Training - no TensorFlow)
echo  [3] Run All     (Tasks 1 + 2 in sequence)
echo  [4] Launch GUI  (Desktop App)
echo  [5] Exit
echo.
set /p choice="Enter choice [1-5]: "

if "%choice%"=="1" ( python run_all.py --task 1 & pause & goto end )
if "%choice%"=="2" ( python run_all.py --task 2 & pause & goto end )
if "%choice%"=="3" ( python run_all.py & pause & goto end )
if "%choice%"=="4" ( python GUI\engine_gui.py & goto end )
:end
