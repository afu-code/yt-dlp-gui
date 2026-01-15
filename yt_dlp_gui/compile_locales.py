
import os
import struct

def msgfmt(po_file, mo_file):
    """
    Improved PO to MO compiler that handles multi-line strings and escapes.
    """
    messages = {}
    with open(po_file, 'r', encoding='utf-8') as f:
        id_accum = None
        str_accum = ""
        mode = None # "id" or "str"
        
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            if line.startswith('msgid "'):
                if id_accum is not None:
                    messages[id_accum] = str_accum
                id_accum = line[7:-1]
                str_accum = ""
                mode = "id"
            elif line.startswith('msgstr "'):
                str_accum = line[8:-1]
                mode = "str"
            elif line.startswith('"'):
                content = line[1:-1]
                if mode == "id":
                    id_accum += content
                elif mode == "str":
                    str_accum += content
        
        if id_accum is not None:
            messages[id_accum] = str_accum

    def fix_escapes(s):
        # Handle essential escapes for gettext
        return s.replace('\\n', '\n').replace('\\"', '"').replace('\\\\', '\\')

    processed_messages = {}
    for k, v in messages.items():
        processed_messages[fix_escapes(k)] = fix_escapes(v)
    
    messages = processed_messages

    keys = sorted(messages.keys())
    offsets = []
    ids = b''
    strs = b''
    
    for k in keys:
        v = messages[k].encode('utf-8')
        k_bytes = k.encode('utf-8')
        offsets.append((len(ids), len(k_bytes), len(strs), len(v)))
        ids += k_bytes + b'\0'
        strs += v + b'\0'

    nstrings = len(keys)
    keystart = 28
    valstart = keystart + 8 * nstrings
    data_start = valstart + 8 * nstrings
    
    header = struct.pack('<IIIIIII',
                         0x950412de, # magic
                         0,          # version
                         nstrings,
                         keystart,
                         valstart,
                         0, data_start) 
    
    keytable = b''
    valtable = b''
    for id_off, id_len, str_off, str_len in offsets:
        keytable += struct.pack('<II', id_len, data_start + id_off)
        valtable += struct.pack('<II', str_len, data_start + len(ids) + str_off)
        
    final_mo = header + keytable + valtable + ids + strs
    
    with open(mo_file, 'wb') as f:
        f.write(final_mo)

def main():
    base_dir = os.path.join(os.path.dirname(__file__), "locales")
    for lang in os.listdir(base_dir):
        lang_dir = os.path.join(base_dir, lang, "LC_MESSAGES")
        if os.path.isdir(lang_dir):
            po_path = os.path.join(lang_dir, "yt_dlp_gui.po")
            mo_path = os.path.join(lang_dir, "yt_dlp_gui.mo")
            if os.path.exists(po_path):
                print(f"Compiling {po_path} -> {mo_path}")
                try:
                    msgfmt(po_path, mo_path)
                except Exception as e:
                    print(f"Failed to compile {lang}: {e}")

if __name__ == "__main__":
    main()
