import openvds

url = "http://node3:9000/vds-demo?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ESTRUCNTRAB6N2N8P1PZ%2F20240420%2Fvn-north-1%2Fs3%2Faws4_request&X-Amz-Date=20240420T222214Z&X-Amz-Expires=43200&X-Amz-Security-Token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiJFU1RSVUNOVFJBQjZOMk44UDFQWiIsImV4cCI6MTcxMzY3MzczNCwicGFyZW50IjoibWluaW9hZG1pbiJ9.OVO3UYZwvRC4cHgLgTvC6rsBz6J7PcbXnP7GJQwPnYQFYke7jdQXLQdRWgnBhu9zv2MS1E7WnPNHDrEFaLbHFg&X-Amz-SignedHeaders=host&versionId=null&X-Amz-Signature=3cbc5a912f0733431b61984a241c2d0bc26e5566cf4768e8661b50051aac93ec"
# url = "http://os-support-94/api/swift/containers/test/object/vdstest"
# url = "http://node3:9000/vds-demo/Seismic.vds?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-SignedHeaders=host&X-Amz-Credential=DojZFN4YxfiVMoAEhD7q%2F20240420%2Fvn-north-1%2Fs3%2Faws4_request&X-Amz-Date=20240420T181455Z&X-Amz-Expires=604800&X-Amz-Signature=af7761918493f0019d2f0d54f1b31d4c162ce21ef5439c79f5eca451e05c1add"
connection = "Region=vn-north-1"


try:
    with openvds.open(url) as vds:
        print(vds)
        # manager = openvds.getAccessManager(vds)
        # layout = manager.volumeDataLayout
        # sampleDimension, crosslineDimension, inlineDimension = (0, 1, 2)
        # inlineAxis = layout.getAxisDescriptor(inlineDimension)
        # inlineNumber = (inlineAxis.coordinateMin + inlineAxis.coordinateMax) // 2
        # inlineIndex = inlineAxis.coordinateToSampleIndex(inlineNumber)
        # print(inlineAxis, inlineNumber, inlineIndex)
except RuntimeError as error:
    print(f"Could not open VDS: {error}")
