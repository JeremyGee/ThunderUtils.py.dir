from __future__ import with_statement

import random

from Helper import color

import org.bukkit as bukkit

derps = []

def load_derps(filename):
    global derps
    
    with open(filename) as f:
            derps = f.read().splitlines()

def broadcast_derp(sender, message):
    bukkit.Bukkit.broadcastMessage(''.join([color("2"), " * ", color("f"), sender.getName(), color("l"), " DERP! ", color("r"), color("d"),  message]))

@hook.command("derp", description="Let your derp shine!")
def onCommandDerp(sender, args):
    if len(args) > 0:
        broadcast_derp(sender, derps[int(args[0])])
    else:
        broadcast_derp(sender, random.choice(derps))

    return True

@hook.command("derps", description="List available derps")
def onCommandDerps(sender, args):
    for counter in xrange(len(derps)):
        sender.sendMessage(''.join([color("1"), str(counter), color("f"), ": ", color("a"), derps[counter]]))

    return True
