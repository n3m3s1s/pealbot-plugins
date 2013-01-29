# coding: utf-8
"""
Copyright (c) 2012 

   Julian Held <nemesis@creative-heads.org>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from plugin import Plugin
from random import shuffle
 
class Greeter(Plugin):
        voices = ['Einen wunderschönen guten Tag, %s', 'Oh Gott...%s? Ich verkriech mich unterm Tisch. Bis dann!', '%s, wir grüßen euch und eure Gefolgschaft', 'Howdy, %s', '%s entert das sinkene Schiff!', 'Aloha, %s', 'Die Macht sei mit dir, junger %s']
 
        def __init__(self, bot):
                Plugin.__init__(self, bot)
                self.subscribe("irc.join", self.onjoin)
 
        def get_random(self):
                if not self.voices:
                        return "Hi, %s"
                else:
                        shuffle(self.voices)
                        return self.voices[0]
 
        def onjoin(self, msg):
                chan = msg.params[0]
                voice = self.get_random()
                self.bot.msg(chan, voice % msg.nick)
