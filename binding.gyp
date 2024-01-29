{
  'targets': [{
    'target_name': 'windowutilsjs',
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'xcode_settings': { 'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'CLANG_CXX_LIBRARY': 'libc++',
        'MACOSX_DEPLOYMENT_TARGET': '10.7',
        'OTHER_CFLAGS': [
          '-arch x86_64',
          '-arch arm64'
        ],
        'OTHER_LDFLAGS': [
          '-arch x86_64',
          '-arch arm64'
        ]
      },
      'msvs_settings': {
        'VCCLCompilerTool': { 'ExceptionHandling': 1 },
      },
    
    'include_dirs': [
      '<!(node -p "require(\'node-addon-api\').include_dir")',
    ],
    'conditions': [
      ['OS == "mac"', {
        'sources': [
          'src/mac/windowutils.mm'
        ],
        'include_dirs': [
          '<!(node -p "require(\'node-addon-api\').include_dir")',
          'System/Library/Frameworks/Carbon.Framework/Headers',
        ],
        'link_settings': {
          'libraries': [
            '-framework Carbon',
            '-framework AppKit',
          ]
        },
        'xcode_settings': {
            'OTHER_CFLAGS': [
                '-ObjC++'
            ]
        }
      }],
      ["OS=='win'", {
        'sources': [
          'src/win/windowutils.cc'
        ],
        'msvs_settings': {
            'VCCLCompilerTool': { "ExceptionHandling": 1 }
        }
      }],
      ['OS == "linux"', {
        'sources': [
          'src/unsupported/windowutils.cc'
        ]
      }],     
    ],
    'sources': [ 'src/windowutils.cc'],
  }],
}