
#include "../windowutils.h"
#include <napi.h>
#import <Foundation/Foundation.h>
#import <AppKit/AppKit.h>

Napi::Value getWindowTitle(Napi::Env env, unsigned char* buffer) {
  NSView* view = *reinterpret_cast<NSView**>(buffer);
  if (!view)
      return Napi::String::New(env, "");

  NSWindow* window = [view window];
  NSString* title = [window title];
  return Napi::String::New(env, [title UTF8String]);
}


Napi::Value allowWindowFullScreenTiling(Napi::Env env, unsigned char* buffer){
  NSView* view = *reinterpret_cast<NSView**>(buffer);
  if (!view)
      return Napi::String::New(env, "");

  NSWindow* window = [view window];

  window.collectionBehavior = NSWindowCollectionBehaviorFullScreenAllowsTiling;
  
  return Napi::Boolean::New(env, true);
}