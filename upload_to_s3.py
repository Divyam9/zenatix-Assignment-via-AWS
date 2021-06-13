import boto
import boto.s3
import sys
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = "AKIAZC7FEMFA2O5JXJ6J"
AWS_SECRET_ACCESS_KEY = "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"

bucket_name = AWS_ACCESS_KEY_ID.lower() + "-temp"
conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)


bucket = conn.create_bucket(bucket_name, location=boto.s3.connection.Location.DEFAULT)

testfile = "file.txt"

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


k = Key(bucket)
k.key = "test file"
k.set_contents_from_filename(testfile, cb=percent_cb, num_cb=10)