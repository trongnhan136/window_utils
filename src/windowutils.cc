#include <napi.h>
#include "windowutils.h"

namespace WindowUtilsJS {
Napi::Value getWindowTitleWrapper(const Napi::CallbackInfo& info)
{
	Napi::Env env = info.Env();
	auto buffer = info[0].As<Napi::Buffer<char>>().Data();
	return getWindowTitle(env, (unsigned char*)buffer);
}

Napi::Value allowWindowFullScreenTilingWrapper(const Napi::CallbackInfo& info)
{
	Napi::Env env = info.Env();
	auto buffer = info[0].As<Napi::Buffer<char>>().Data();
	return allowWindowFullScreenTiling(env, (unsigned char*)buffer);
}



Napi::Object InitAll(Napi::Env env, Napi::Object exports){
    exports.Set(Napi::String::New(env, "getWindowTitle"),
				Napi::Function::New(env, getWindowTitleWrapper));
	exports.Set(Napi::String::New(env, "allowWindowFullScreenTiling"),
				Napi::Function::New(env, allowWindowFullScreenTilingWrapper));
    return exports;
}
NODE_API_MODULE(fullscreenjs, InitAll)
}

