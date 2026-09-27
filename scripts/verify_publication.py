"""Verify preserved research bytes and replay the immutable original release.

Publication overlays are explicitly excluded from the original-byte comparison;
the original archive verifier is never relaxed or rewritten.
"""
from pathlib import Path
import argparse, hashlib, json, subprocess, sys, tempfile, urllib.request, zipfile
ROOT=Path(__file__).resolve().parents[1]
CONFIG={'repo': 'AIAP', 'sha256': 'db58b397ceba7a642efd5ce38fa39777355fb14a1442682cbd80bcaa86e30943', 'root': 'AIAP_v6.5_COMPLETE_READY', 'verifier': '08_VERIFICATION/verify_release.py', 'overlay': ['README.md', 'LICENSE.md', 'RIGHTS_AND_LICENSING.md', 'CITATION.cff', 'START_HERE.md'], 'url': 'https://github.com/MathGov/AIAP/releases/download/AIAP-v6.5/AIAP_v6.5_COMPLETE_READY_FINAL.zip'}
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--archive', type=Path, help='Use a previously downloaded original ZIP')
    args=parser.parse_args()
    original=json.loads((ROOT/'provenance/ORIGINAL_REPOSITORY_SHA256.json').read_text(encoding='utf-8'))
    failed=[]
    for name, expected in original.items():
        if name in CONFIG['overlay']: continue
        p=ROOT/name
        if not p.is_file():
            failed.append(name); continue
        data=p.read_bytes()
        if expected['normalize_crlf']: data=data.replace(b'\r\n',b'\n')
        if hashlib.sha256(data).hexdigest()!=expected['sha256']: failed.append(name)
    if failed: raise SystemExit('Preserved-file mismatch: '+', '.join(failed))
    print('PASS: preserved repository payload',len(original)-len(CONFIG['overlay']),'files',flush=True)
    with tempfile.TemporaryDirectory(prefix='publication-verify-') as tmp:
        tmp=Path(tmp)
        archive=args.archive.resolve() if args.archive else tmp/'original.zip'
        if not args.archive:
            urllib.request.urlretrieve(CONFIG['url'],archive)
        if digest(archive)!=CONFIG['sha256']: raise SystemExit('Original archive SHA-256 mismatch')
        target=tmp/'extracted'
        target.mkdir()
        with zipfile.ZipFile(archive) as z:
            for member in z.infolist():
                if not (target/member.filename).resolve().is_relative_to(target.resolve()):
                    raise SystemExit('Unsafe archive member')
            z.extractall(target)
        package=target/CONFIG['root']
        command=[sys.executable,'-B',str(package/CONFIG['verifier'])]
        if CONFIG['repo']=='AIAP': command.append(str(package))
        subprocess.run(command,cwd=package,check=True)
    if CONFIG['repo']=='AIAP':
        subprocess.run([sys.executable,'-B','-m','unittest','-v','test_validate_aiap_record.py'],cwd=ROOT/'06_MACHINE_READABLE',check=True)
    print('PASS: publication integrity and original release verification; not empirical validation.')
if __name__=='__main__': main()
