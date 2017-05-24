#This stores the location of the file and installs it silently (/s) , (/v) passes arguments to msiexec
#...so it passes (/qn) which means run with no UI

$pathvargs = {S:\Druva\inSync-5.9-r51251.msi /S /v/qn }
Invoke-Command -ScriptBlock $pathvargs