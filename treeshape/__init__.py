#  treeshape: quickly make file and directory structures.
#
# Copyright (c) 2012, Jonathan Lange <jml@mumak.net>
#
# Licensed under either the Apache License, Version 2.0 or the BSD 3-clause
# license at the users choice. A copy of both licenses are available in the
# project source as Apache-2.0 and BSD. You may not use this file except in
# compliance with one of these two licences.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under these licenses is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# license you chose for the specific language governing permissions and
# limitations under that license.

"""treeshape"""

__all__ = [
    'FileTree',
    'make_tree',
    ]


from ._fixtures import FileTree
from ._treeshape import make_tree
