import io
import sys
import tarfile

package_path = "/tmp/package/"
sys.path.append(package_path)
tarfile.TarFile.chown = lambda *_, **__: None


def load_package_buffer(buffer):
    fd = io.BytesIO(buffer.to_py())
    with tarfile.TarFile(fileobj=fd) as zf:
        zf.extractall(package_path)

    from core.checker import check_entry
    from core.pyodide_helpers import install_imports
    from core.text import load_chapters
    from core import translation as t

    # t.set_language("es")

    list(load_chapters())

    return dict(
        check_entry=check_entry,
        install_imports=install_imports,
    )
