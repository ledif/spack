##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install stapl
#
# You can edit this file again by typing:
#
#     spack edit stapl
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Stapl(Package):
    """STAPL: A standard library for modern high-performance C++"""

    homepage = "https://parasol-lab.gitlab.io/stapl-home/"

    version('0.1.0', git='git@gitlab.com:parasol-lab/stapl', tag='v0.1.0')

    variant('openmp', default=False, description="Enable OpenMP support")

    depends_on('boost@1.56.0')
    depends_on('mpi')

    def setup_environment(self, spack_env, run_env):
      build_path = join_path(self.stage.path, 'stapl')
      spack_env.set('STAPL', build_path)
      spack_env.set('platform', 'LINUX_gcc')
      spack_env.set('stl', './tools/libstdc++/5.4.0')
      #spack_env.set('BOOST_ROOT', '???')

    def install(self, spec, prefix):
      env['CC'] = spec['mpi'].mpicc
      env['CXX'] = spec['mpi'].mpicxx
      env['BOOST_ROOT'] = spec['boost'].prefix
      #env['platform'] = 'LINUX_gcc'
      #env['stl'] = ''

      #stl_version="not_found"
      #if spec.satifies("gcc@4.9.3"):
      #  stl_version="4.9.3"

      make()
#        make('install')
