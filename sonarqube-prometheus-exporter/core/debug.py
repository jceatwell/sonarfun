import debugpy
import prometheus_exporter

print("waiting for attachment")

debugpy.listen(5678)
debugpy.wait_for_client()  # blocks execution until client is attached

print("Now Debugging in live container")
prometheus_exporter.main()