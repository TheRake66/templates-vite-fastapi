for /D %%d in (*) do (
  powershell -Command "Compress-Archive -Path '%%d\*' -DestinationPath '%%d.zip' -Force"
)