@echo off
REM ============================================================
REM  Lancement du script h5_to_csv_gui dans l'environnement Py26
REM ============================================================

setlocal

REM --- Detection universelle de conda.bat (fonctionne sur tout poste) ---
call :find_conda
if not defined CONDA_BAT (
    echo [ERREUR] conda.bat introuvable.
    echo Installez Miniconda/Anaconda ou ajoutez "condabin" au PATH.
    pause
    exit /b 1
)

REM Se placer dans le dossier du .bat (le script h5_to_csv_gui.py doit etre a cote)
cd /d "%~dp0"

echo === Activation de Py26 ===
call "%CONDA_BAT%" activate Py26

echo === Lancement de h5_to_csv_gui ===
python h5_to_csv_gui.py

echo.
pause
goto :eof

REM ============================================================
REM  Sous-routines
REM ============================================================

REM ---- Detection de conda.bat : positionne la variable CONDA_BAT ----
:find_conda
set "CONDA_BAT="
REM 1) condabin present dans le PATH
for /f "delims=" %%I in ('where conda.bat 2^>nul') do if not defined CONDA_BAT set "CONDA_BAT=%%I"
if defined CONDA_BAT goto :eof
REM 2) via la variable CONDA_EXE (conda deja initialise)
if defined CONDA_EXE for %%I in ("%CONDA_EXE%") do if exist "%%~dpI..\condabin\conda.bat" set "CONDA_BAT=%%~dpI..\condabin\conda.bat"
if defined CONDA_BAT goto :eof
REM 3) emplacements d'installation classiques
for %%P in (
  "%USERPROFILE%\miniconda3"
  "%USERPROFILE%\anaconda3"
  "%USERPROFILE%\Miniconda3"
  "%USERPROFILE%\Anaconda3"
  "%LOCALAPPDATA%\miniconda3"
  "%LOCALAPPDATA%\anaconda3"
  "%LOCALAPPDATA%\Continuum\anaconda3"
  "%LOCALAPPDATA%\Continuum\miniconda3"
  "C:\ProgramData\miniconda3"
  "C:\ProgramData\anaconda3"
  "C:\ProgramData\Miniconda3"
  "C:\ProgramData\Anaconda3"
  "C:\miniconda3"
  "C:\anaconda3"
) do if not defined CONDA_BAT if exist "%%~P\condabin\conda.bat" set "CONDA_BAT=%%~P\condabin\conda.bat"
goto :eof
