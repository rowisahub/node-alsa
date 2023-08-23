{
  "targets": [
    {
      "target_name": "alsa",
      "sources": [ "alsa.cc", "pcm.cc" ],
      "libraries": [ "-lasound" ]
    }
  ],
  "include_dirs" : [
    "<!(node -e \"require('nan')\")"
  ]
}
