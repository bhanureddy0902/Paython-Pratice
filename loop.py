from minio import Minio
import os
import time
start_time = time.time()
client= Minio(
    "play.min.io",
    access_key="Q3AM3UQ867SPQQA43P2F",
    secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
)
#buckets=client.list_buckets()
#for bucket in buckets:
    #print(bucket.name, bucket.creation_date)
my_path = r"C:\Users\bhanu\Desktop\jsonfile"
i = 1
while i <= 100000:
    for filename in os.listdir(my_path):
        if filename.endswith(".json"+str(i)):
            result = client.fput_object(
                "filesuploadedbyloop",
                filename,
                os.path.join(my_path, filename),

            )
            print(
                "Created {0} object; etag: {1}, version-id: {2}".format(
                    result.object_name, result.etag, result.version_id
                )
            )
    i += 1

end_time = time.time()
print("total time taken is {}".format(end_time - start_time))