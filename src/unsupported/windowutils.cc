#include <napi.h>
#include "../windowutils.h"

Napi::Value getWindowTitle(Napi::Env env, unsigned char* buffer) {
  return Napi::String::New(env, "");
}
