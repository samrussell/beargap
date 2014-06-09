#!/usr/bin/python

from sys import argv
import zbar
import re
import base64

# create a Processor
proc = zbar.Processor()

# configure the Processor
proc.parse_config('enable')

# initialize the Processor
device = '/dev/video0'
if len(argv) > 1:
    device = argv[1]
proc.init(device)

class beargapdata:
  def __init__(self):
    self.qrs={}
    self.sha=None
    self.total=0

data = beargapdata()

# setup a callback
def my_handler(proc, image, closure):
    # extract results
    for symbol in image:
        #if not symbol.count:
        try:
            # do something useful with results
            #print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
            # parse, check if valid bearcode:
            m = re.search(r"bearcode:([0-9a-f]{64})\[([0-9]+)of([0-9]+)\]\s(.*)", symbol.data)
            if m:
              # check if we have hash
              sha = m.group(1)
              num = int(m.group(2))
              total = int(m.group(3))
              code = m.group(4)
              if not data.sha:
                # set up data
                data.sha = sha
                data.total = total

              # if hash matches then add to qrs
              if sha == data.sha:
                data.qrs[num] = code
                print "Got QR %d of %d" % (num, total)
              else:
                print "Read hash %s, expected hash %s" % (sha, data.sha)

              # check what is left
              finished = True
              wholecode = ""
              for i in range(data.total):
                if i+1 not in data.qrs:
                  finished = False
                else:
                  wholecode = wholecode + data.qrs[i+1]
              if finished:
                print "All codes captured, output:"
                print base64.b64decode(wholecode)


            else:
              print "Matched a code but not a bearcode"
        except Exception as e:
          print e
          raise e
        


proc.set_data_handler(my_handler)

# enable the preview window
proc.visible = True

# initiate scanning
proc.active = True
try:
    proc.user_wait()
except zbar.WindowClosed:
    pass
