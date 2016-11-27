# OS-OPERATIONS


1. PYTHON OS MODULE

This module provides a portable way of using operating system dependent functionality. If you just want to read or write a file see open(), if you want to manipulate paths, see the os.path module, and if you want to read all the lines in all the files on the command line see the fileinput module. For creating temporary files and directories see the tempfile module, and for high-level file and directory handling see the shutil module.

Notes on the availability of these functions:

The design of all built-in operating system dependent modules of Python is such that as long as the same functionality is available, it uses the same interface; for example, the function os.stat(path) returns stat information about path in the same format (which happens to have originated with the POSIX interface).
Extensions peculiar to a particular operating system are also available through the os module, but using them is of course a threat to portability.
An “Availability: Unix” note means that this function is commonly found on Unix systems. It does not make any claims about its existence on a specific operating system.
If not separately noted, all functions that claim “Availability: Unix” are supported on Mac OS X, which builds on a Unix core.


2. PYTHON SHUTIL MODULE

The shutil module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal. For operations on individual files

hutil.copyfileobj(fsrc, fdst[, length])
Copy the contents of the file-like object fsrc to the file-like object fdst. The integer length, if given, is the buffer size. In particular, a negative length value means to copy the data without looping over the source data in chunks; by default the data is read in chunks to avoid uncontrolled memory consumption. Note that if the current file position of the fsrc object is not 0, only the contents from the current file position to the end of the file will be copied.

shutil.copyfile(src, dst)
Copy the contents (no metadata) of the file named src to a file named dst. dst must be the complete target file name; look at shutil.copy() for a copy that accepts a target directory path. If src and dst are the same files, Error is raised. The destination location must be writable; otherwise, an IOError exception will be raised. If dst already exists, it will be replaced. Special files such as character or block devices and pipes cannot be copied with this function. src and dst are path names given as strings.

shutil.copymode(src, dst)
Copy the permission bits from src to dst. The file contents, owner, and group are unaffected. src and dst are path names given as strings.

shutil.copystat(src, dst)
Copy the permission bits, last access time, last modification time, and flags from src to dst. The file contents, owner, and group are unaffected. src and dst are path names given as strings.

shutil.copy(src, dst)
Copy the file src to the file or directory dst. If dst is a directory, a file with the same basename as src is created (or overwritten) in the directory specified. Permission bits are copied. src and dst are path names given as strings.

shutil.copy2(src, dst)
Similar to shutil.copy(), but metadata is copied as well – in fact, this is just shutil.copy() followed by copystat(). This is similar to the Unix command cp -p.

shutil.ignore_patterns(*patterns)
This factory function creates a function that can be used as a callable for copytree()‘s ignore argument, ignoring files and directories that match one of the glob-style patterns provided. See the example below.

New in version 2.6.

shutil.copytree(src, dst, symlinks=False, ignore=None)
Recursively copy an entire directory tree rooted at src. The destination directory, named by dst, must not already exist; it will be created as well as missing parent directories. Permissions and times of directories are copied with copystat(), individual files are copied using shutil.copy2().

If symlinks is true, symbolic links in the source tree are represented as symbolic links in the new tree, but the metadata of the original links is NOT copied; if false or omitted, the contents and metadata of the linked files are copied to the new tree.

If ignore is given, it must be a callable that will receive as its arguments the directory being visited by copytree(), and a list of its contents, as returned by os.listdir(). Since copytree() is called recursively, the ignore callable will be called once for each directory that is copied. The callable must return a sequence of directory and file names relative to the current directory (i.e. a subset of the items in its second argument); these names will then be ignored in the copy process. ignore_patterns() can be used to create such a callable that ignores names based on glob-style patterns.

If exception(s) occur, an Error is raised with a list of reasons.

The source code for this should be considered an example rather than the ultimate tool.

Changed in version 2.3: Error is raised if any exceptions occur during copying, rather than printing a message.

Changed in version 2.5: Create intermediate directories needed to create dst, rather than raising an error. Copy permissions and times of directories using copystat().

Changed in version 2.6: Added the ignore argument to be able to influence what is being copied.

shutil.rmtree(path[, ignore_errors[, onerror]])
Delete an entire directory tree; path must point to a directory (but not a symbolic link to a directory). If ignore_errors is true, errors resulting from failed removals will be ignored; if false or omitted, such errors are handled by calling a handler specified by onerror or, if that is omitted, they raise an exception.

If onerror is provided, it must be a callable that accepts three parameters: function, path, and excinfo. The first parameter, function, is the function which raised the exception; it will be os.path.islink(), os.listdir(), os.remove() or os.rmdir(). The second parameter, path, will be the path name passed to function. The third parameter, excinfo, will be the exception information return by sys.exc_info(). Exceptions raised by onerror will not be caught.

Changed in version 2.6: Explicitly check for path being a symbolic link and raise OSError in that case.

shutil.move(src, dst)
Recursively move a file or directory (src) to another location (dst).

If the destination is an existing directory, then src is moved inside that directory. If the destination already exists but is not a directory, it may be overwritten depending on os.rename() semantics.

If the destination is on the current filesystem, then os.rename() is used. Otherwise, src is copied (using shutil.copy2()) to dst and then removed.

New in version 2.3.




