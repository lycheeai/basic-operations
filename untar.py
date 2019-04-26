import tarfile

def untar(file_generator):
  for file in file_generator:
    with tarfile.open(file.result.name, 'r') as tf:
      for entry in tf:
        yield PipelineSuccess(file.name + '/' + entry.name, tf.open(entry, 'r'))
