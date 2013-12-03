#!/usr/bin/env python

import sys
import Evernote.writer as Output
import Tomboy.reader as Import

def main():
    collection = Output.Collection(sys.stdout)
    for filename in sys.argv[1:]:
        incoming = Import.Note(filename)
        collection.addNote(Output.Note(
            title = incoming.title,
            lastchange = incoming.lastchange,
            created = incoming.created,
            content = incoming.body_html
        ))

    collection.save()


if __name__ == '__main__':
    main()


