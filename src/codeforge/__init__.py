"""CodeForge - منشئ المشاريع البرمجية"""

from .core.version import get_version, get_version_tuple, print_version

__version__ = get_version()
__version_tuple__ = get_version_tuple()
__author__ = "مطور CodeForge"

# إعادة تصدير الدوال المهمة
__all__ = [
    "get_version",
    "print_version",
    "__version__",
    "__author__",
]

