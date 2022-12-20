# Triggered by a change in a storage bucket

import base64
import os
import shutil
import logging
import tempfile
import functions_framework
import git
from os.path import exists
from google.cloud import storage
from google.cloud.storage.blob import Blob
from git import Repo

@functions_framework.cloud_event
def hello_gcs(cloud_event):
  data = cloud_event.data

  event_id = cloud_event["id"]
  event_type = cloud_event["type"]

  bucket = data["bucket"]
  file_path = data["name"]
  metageneration = data["metageneration"]
  timeCreated = data["timeCreated"]
  updated = data["updated"]

  print(f"Event ID: {event_id}")
  print(f"Event type: {event_type}")
  print(f"Bucket: {bucket}")
  print(f"File: {file_path}")
  print(f"Metageneration: {metageneration}")
  print(f"Created: {timeCreated}")
  print(f"Updated: {updated}")
  if ".parquet" in file_path:
    if "output-00000" in file_path:
      file_name = file_path.split("/",1)[0]
      print("Renamed file to " + file_name)
    else:
      print("Oh, uh, nevermind. File name is already right")
    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(file_path)
    folder = "/tmp/repo"
    if os.path.exists(folder):
      print("No worries, the folder exists")
    else:
      os.mkdir(folder)
    short_name = os.path.basename(blob.name)
    logging.info("Blobs: {}".format(short_name))
    destination_uri = folder + "/" + short_name

    repo_dir = "/tmp/repo"
    if os.path.exists(repo_dir):
      shutil.rmtree(repo_dir, ignore_errors=True)
      os.mkdir(repo_dir)
    else:
      os.mkdir(repo_dir)
    user_email = "23001651+shanecglass@users.noreply.github.com"
    user_name = "shanecglass"
    password = os.environ.get("GITHUB-PAT")
    print("Auth information and file to commit defined")

    remote_repo = f"https://{user_name}:{password}@github.com/shanecglass/malloy_demos.git"
    print(remote_repo)
    Repo.clone_from(remote_repo, repo_dir, branch = "main")
    repo = git.Repo(repo_dir)
    print("repo cloned")

    destination_folder = folder + "/political_ads"
    destination_uri = destination_folder + "/"+ file_name
    if os.path.exists(destination_folder):
      blob.download_to_filename(destination_uri)
    else:
      os.mkdir(destination_folder)
      blob.download_to_filename(destination_uri)
    logging.info("Exported {} to {}".format(blob, destination_uri))
    print("File downloaded: " + file_name)

    file_to_commit = file_name
    file_path_to_commit = destination_uri
    commit_message = 'Updating data'
    repo.index.add(file_path_to_commit)
    repo.index.commit(commit_message)
    origin = repo.remote(name="origin")
    origin.push()
    print("Commit complete")
  else:
    print("These are intermediate files. We're ignoring them")
