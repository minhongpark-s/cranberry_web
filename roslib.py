__all__ = ['roslib']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
def PyJs_LONG_319_(var=var):
    @Js
    def PyJs_anonymous_0_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['module', 'require', 'exports'])
        @Js
        def PyJs_anonymous_1_(PyJsArg_676c6f62616c_, undefined, this, arguments, var=var):
            var = Scope({'global':PyJsArg_676c6f62616c_, 'undefined':undefined, 'this':this, 'arguments':arguments}, var)
            var.registers(['decode', 'POW_2_24', 'obj', 'POW_2_32', 'undefined', 'global', 'POW_2_53', 'encode'])
            @Js
            def PyJsHoisted_encode_(value, this, arguments, var=var):
                var = Scope({'value':value, 'this':this, 'arguments':arguments}, var)
                var.registers(['writeUint8Array', 'writeUint16', 'writeUint32', 'writeUint8', 'ret', 'lastLength', 'retView', 'writeUint64', 'dataView', 'data', 'offset', 'write', 'writeTypeAndLength', 'ensureSpace', 'writeFloat64', 'value', 'i', 'encodeItem'])
                @Js
                def PyJsHoisted_ensureSpace_(length, this, arguments, var=var):
                    var = Scope({'length':length, 'this':this, 'arguments':arguments}, var)
                    var.registers(['newByteLength', 'uint32count', 'length', 'requiredLength', 'oldDataView', 'i'])
                    var.put('newByteLength', var.get('data').get('byteLength'))
                    var.put('requiredLength', (var.get('offset')+var.get('length')))
                    while (var.get('newByteLength')<var.get('requiredLength')):
                        var.put('newByteLength', Js(2.0), '*')
                    if PyJsStrictNeq(var.get('newByteLength'),var.get('data').get('byteLength')):
                        var.put('oldDataView', var.get('dataView'))
                        var.put('data', var.get('ArrayBuffer').create(var.get('newByteLength')))
                        var.put('dataView', var.get('DataView').create(var.get('data')))
                        var.put('uint32count', ((var.get('offset')+Js(3.0))>>Js(2.0)))
                        #for JS loop
                        var.put('i', Js(0.0))
                        while (var.get('i')<var.get('uint32count')):
                            try:
                                var.get('dataView').callprop('setUint32', (var.get('i')*Js(4.0)), var.get('oldDataView').callprop('getUint32', (var.get('i')*Js(4.0))))
                            finally:
                                    var.put('i',Js(var.get('i').to_number())+Js(1))
                    var.put('lastLength', var.get('length'))
                    return var.get('dataView')
                PyJsHoisted_ensureSpace_.func_name = 'ensureSpace'
                var.put('ensureSpace', PyJsHoisted_ensureSpace_)
                @Js
                def PyJsHoisted_write_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    var.put('offset', var.get('lastLength'), '+')
                PyJsHoisted_write_.func_name = 'write'
                var.put('write', PyJsHoisted_write_)
                @Js
                def PyJsHoisted_writeFloat64_(value, this, arguments, var=var):
                    var = Scope({'value':value, 'this':this, 'arguments':arguments}, var)
                    var.registers(['value'])
                    var.get('write')(var.get('ensureSpace')(Js(8.0)).callprop('setFloat64', var.get('offset'), var.get('value')))
                PyJsHoisted_writeFloat64_.func_name = 'writeFloat64'
                var.put('writeFloat64', PyJsHoisted_writeFloat64_)
                @Js
                def PyJsHoisted_writeUint8_(value, this, arguments, var=var):
                    var = Scope({'value':value, 'this':this, 'arguments':arguments}, var)
                    var.registers(['value'])
                    var.get('write')(var.get('ensureSpace')(Js(1.0)).callprop('setUint8', var.get('offset'), var.get('value')))
                PyJsHoisted_writeUint8_.func_name = 'writeUint8'
                var.put('writeUint8', PyJsHoisted_writeUint8_)
                @Js
                def PyJsHoisted_writeUint8Array_(value, this, arguments, var=var):
                    var = Scope({'value':value, 'this':this, 'arguments':arguments}, var)
                    var.registers(['value', 'dataView', 'i'])
                    var.put('dataView', var.get('ensureSpace')(var.get('value').get('length')))
                    #for JS loop
                    var.put('i', Js(0.0))
                    while (var.get('i')<var.get('value').get('length')):
                        try:
                            var.get('dataView').callprop('setUint8', (var.get('offset')+var.get('i')), var.get('value').get(var.get('i')))
                        finally:
                                var.put('i',Js(var.get('i').to_number())+Js(1))
                    var.get('write')()
                PyJsHoisted_writeUint8Array_.func_name = 'writeUint8Array'
                var.put('writeUint8Array', PyJsHoisted_writeUint8Array_)
                @Js
                def PyJsHoisted_writeUint16_(value, this, arguments, var=var):
                    var = Scope({'value':value, 'this':this, 'arguments':arguments}, var)
                    var.registers(['value'])
                    var.get('write')(var.get('ensureSpace')(Js(2.0)).callprop('setUint16', var.get('offset'), var.get('value')))
                PyJsHoisted_writeUint16_.func_name = 'writeUint16'
                var.put('writeUint16', PyJsHoisted_writeUint16_)
                @Js
                def PyJsHoisted_writeUint32_(value, this, arguments, var=var):
                    var = Scope({'value':value, 'this':this, 'arguments':arguments}, var)
                    var.registers(['value'])
                    var.get('write')(var.get('ensureSpace')(Js(4.0)).callprop('setUint32', var.get('offset'), var.get('value')))
                PyJsHoisted_writeUint32_.func_name = 'writeUint32'
                var.put('writeUint32', PyJsHoisted_writeUint32_)
                @Js
                def PyJsHoisted_writeUint64_(value, this, arguments, var=var):
                    var = Scope({'value':value, 'this':this, 'arguments':arguments}, var)
                    var.registers(['dataView', 'value', 'low', 'high'])
                    var.put('low', (var.get('value')%var.get('POW_2_32')))
                    var.put('high', ((var.get('value')-var.get('low'))/var.get('POW_2_32')))
                    var.put('dataView', var.get('ensureSpace')(Js(8.0)))
                    var.get('dataView').callprop('setUint32', var.get('offset'), var.get('high'))
                    var.get('dataView').callprop('setUint32', (var.get('offset')+Js(4.0)), var.get('low'))
                    var.get('write')()
                PyJsHoisted_writeUint64_.func_name = 'writeUint64'
                var.put('writeUint64', PyJsHoisted_writeUint64_)
                @Js
                def PyJsHoisted_writeTypeAndLength_(type, length, this, arguments, var=var):
                    var = Scope({'type':type, 'length':length, 'this':this, 'arguments':arguments}, var)
                    var.registers(['type', 'length'])
                    if (var.get('length')<Js(24.0)):
                        var.get('writeUint8')(((var.get('type')<<Js(5.0))|var.get('length')))
                    else:
                        if (var.get('length')<Js(256)):
                            var.get('writeUint8')(((var.get('type')<<Js(5.0))|Js(24.0)))
                            var.get('writeUint8')(var.get('length'))
                        else:
                            if (var.get('length')<Js(65536)):
                                var.get('writeUint8')(((var.get('type')<<Js(5.0))|Js(25.0)))
                                var.get('writeUint16')(var.get('length'))
                            else:
                                if (var.get('length')<Js(4294967296)):
                                    var.get('writeUint8')(((var.get('type')<<Js(5.0))|Js(26.0)))
                                    var.get('writeUint32')(var.get('length'))
                                else:
                                    var.get('writeUint8')(((var.get('type')<<Js(5.0))|Js(27.0)))
                                    var.get('writeUint64')(var.get('length'))
                PyJsHoisted_writeTypeAndLength_.func_name = 'writeTypeAndLength'
                var.put('writeTypeAndLength', PyJsHoisted_writeTypeAndLength_)
                @Js
                def PyJsHoisted_encodeItem_(value, this, arguments, var=var):
                    var = Scope({'value':value, 'this':this, 'arguments':arguments}, var)
                    var.registers(['utf8data', 'charCode', 'length', 'key', 'keys', 'value', 'i'])
                    pass
                    if PyJsStrictEq(var.get('value'),Js(False)):
                        return var.get('writeUint8')(Js(244))
                    if PyJsStrictEq(var.get('value'),Js(True)):
                        return var.get('writeUint8')(Js(245))
                    if PyJsStrictEq(var.get('value'),var.get(u"null")):
                        return var.get('writeUint8')(Js(246))
                    if PyJsStrictEq(var.get('value'),var.get('undefined')):
                        return var.get('writeUint8')(Js(247))
                    while 1:
                        SWITCHED = False
                        CONDITION = (var.get('value',throw=False).typeof())
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('number')):
                            SWITCHED = True
                            if PyJsStrictEq(var.get('Math').callprop('floor', var.get('value')),var.get('value')):
                                if ((Js(0.0)<=var.get('value')) and (var.get('value')<=var.get('POW_2_53'))):
                                    return var.get('writeTypeAndLength')(Js(0.0), var.get('value'))
                                if (((-var.get('POW_2_53'))<=var.get('value')) and (var.get('value')<Js(0.0))):
                                    return var.get('writeTypeAndLength')(Js(1.0), (-(var.get('value')+Js(1.0))))
                            var.get('writeUint8')(Js(251))
                            return var.get('writeFloat64')(var.get('value'))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('string')):
                            SWITCHED = True
                            var.put('utf8data', Js([]))
                            #for JS loop
                            var.put('i', Js(0.0))
                            while (var.get('i')<var.get('value').get('length')):
                                try:
                                    var.put('charCode', var.get('value').callprop('charCodeAt', var.get('i')))
                                    if (var.get('charCode')<Js(128)):
                                        var.get('utf8data').callprop('push', var.get('charCode'))
                                    else:
                                        if (var.get('charCode')<Js(2048)):
                                            var.get('utf8data').callprop('push', (Js(192)|(var.get('charCode')>>Js(6.0))))
                                            var.get('utf8data').callprop('push', (Js(128)|(var.get('charCode')&Js(63))))
                                        else:
                                            if (var.get('charCode')<Js(55296)):
                                                var.get('utf8data').callprop('push', (Js(224)|(var.get('charCode')>>Js(12.0))))
                                                var.get('utf8data').callprop('push', (Js(128)|((var.get('charCode')>>Js(6.0))&Js(63))))
                                                var.get('utf8data').callprop('push', (Js(128)|(var.get('charCode')&Js(63))))
                                            else:
                                                var.put('charCode', ((var.get('charCode')&Js(1023))<<Js(10.0)))
                                                var.put('charCode', (var.get('value').callprop('charCodeAt', var.put('i',Js(var.get('i').to_number())+Js(1)))&Js(1023)), '|')
                                                var.put('charCode', Js(65536), '+')
                                                var.get('utf8data').callprop('push', (Js(240)|(var.get('charCode')>>Js(18.0))))
                                                var.get('utf8data').callprop('push', (Js(128)|((var.get('charCode')>>Js(12.0))&Js(63))))
                                                var.get('utf8data').callprop('push', (Js(128)|((var.get('charCode')>>Js(6.0))&Js(63))))
                                                var.get('utf8data').callprop('push', (Js(128)|(var.get('charCode')&Js(63))))
                                finally:
                                        var.put('i',Js(var.get('i').to_number())+Js(1))
                            var.get('writeTypeAndLength')(Js(3.0), var.get('utf8data').get('length'))
                            return var.get('writeUint8Array')(var.get('utf8data'))
                        if True:
                            SWITCHED = True
                            pass
                            if var.get('Array').callprop('isArray', var.get('value')):
                                var.put('length', var.get('value').get('length'))
                                var.get('writeTypeAndLength')(Js(4.0), var.get('length'))
                                #for JS loop
                                var.put('i', Js(0.0))
                                while (var.get('i')<var.get('length')):
                                    try:
                                        var.get('encodeItem')(var.get('value').get(var.get('i')))
                                    finally:
                                            var.put('i',Js(var.get('i').to_number())+Js(1))
                            else:
                                if var.get('value').instanceof(var.get('Uint8Array')):
                                    var.get('writeTypeAndLength')(Js(2.0), var.get('value').get('length'))
                                    var.get('writeUint8Array')(var.get('value'))
                                else:
                                    var.put('keys', var.get('Object').callprop('keys', var.get('value')))
                                    var.put('length', var.get('keys').get('length'))
                                    var.get('writeTypeAndLength')(Js(5.0), var.get('length'))
                                    #for JS loop
                                    var.put('i', Js(0.0))
                                    while (var.get('i')<var.get('length')):
                                        try:
                                            var.put('key', var.get('keys').get(var.get('i')))
                                            var.get('encodeItem')(var.get('key'))
                                            var.get('encodeItem')(var.get('value').get(var.get('key')))
                                        finally:
                                                var.put('i',Js(var.get('i').to_number())+Js(1))
                        SWITCHED = True
                        break
                PyJsHoisted_encodeItem_.func_name = 'encodeItem'
                var.put('encodeItem', PyJsHoisted_encodeItem_)
                var.put('data', var.get('ArrayBuffer').create(Js(256.0)))
                var.put('dataView', var.get('DataView').create(var.get('data')))
                pass
                var.put('offset', Js(0.0))
                pass
                pass
                pass
                pass
                pass
                pass
                pass
                pass
                pass
                pass
                var.get('encodeItem')(var.get('value'))
                if var.get('data').contains(Js('slice')):
                    return var.get('data').callprop('slice', Js(0.0), var.get('offset'))
                var.put('ret', var.get('ArrayBuffer').create(var.get('offset')))
                var.put('retView', var.get('DataView').create(var.get('ret')))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('offset')):
                    try:
                        var.get('retView').callprop('setUint8', var.get('i'), var.get('dataView').callprop('getUint8', var.get('i')))
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
                return var.get('ret')
            PyJsHoisted_encode_.func_name = 'encode'
            var.put('encode', PyJsHoisted_encode_)
            @Js
            def PyJsHoisted_decode_(data, tagger, simpleValue, this, arguments, var=var):
                var = Scope({'data':data, 'tagger':tagger, 'simpleValue':simpleValue, 'this':this, 'arguments':arguments}, var)
                var.registers(['readArrayBuffer', 'ret', 'decodeItem', 'offset', 'readUint32', 'readFloat64', 'dataView', 'readUint8', 'simpleValue', 'readIndefiniteStringLength', 'readFloat32', 'readFloat16', 'readUint16', 'data', 'readBreak', 'readUint64', 'tagger', 'readLength', 'appendUtf16data', 'read'])
                @Js
                def PyJsHoisted_read_(value, length, this, arguments, var=var):
                    var = Scope({'value':value, 'length':length, 'this':this, 'arguments':arguments}, var)
                    var.registers(['value', 'length'])
                    var.put('offset', var.get('length'), '+')
                    return var.get('value')
                PyJsHoisted_read_.func_name = 'read'
                var.put('read', PyJsHoisted_read_)
                @Js
                def PyJsHoisted_readArrayBuffer_(length, this, arguments, var=var):
                    var = Scope({'length':length, 'this':this, 'arguments':arguments}, var)
                    var.registers(['length'])
                    return var.get('read')(var.get('Uint8Array').create(var.get('data'), var.get('offset'), var.get('length')), var.get('length'))
                PyJsHoisted_readArrayBuffer_.func_name = 'readArrayBuffer'
                var.put('readArrayBuffer', PyJsHoisted_readArrayBuffer_)
                @Js
                def PyJsHoisted_readFloat16_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers(['sign', 'exponent', 'fraction', 'tempArrayBuffer', 'tempDataView', 'value'])
                    var.put('tempArrayBuffer', var.get('ArrayBuffer').create(Js(4.0)))
                    var.put('tempDataView', var.get('DataView').create(var.get('tempArrayBuffer')))
                    var.put('value', var.get('readUint16')())
                    var.put('sign', (var.get('value')&Js(32768)))
                    var.put('exponent', (var.get('value')&Js(31744)))
                    var.put('fraction', (var.get('value')&Js(1023)))
                    if PyJsStrictEq(var.get('exponent'),Js(31744)):
                        var.put('exponent', (Js(255)<<Js(10.0)))
                    else:
                        if PyJsStrictNeq(var.get('exponent'),Js(0.0)):
                            var.put('exponent', ((Js(127.0)-Js(15.0))<<Js(10.0)), '+')
                        else:
                            if PyJsStrictNeq(var.get('fraction'),Js(0.0)):
                                return (var.get('fraction')*var.get('POW_2_24'))
                    var.get('tempDataView').callprop('setUint32', Js(0.0), (((var.get('sign')<<Js(16.0))|(var.get('exponent')<<Js(13.0)))|(var.get('fraction')<<Js(13.0))))
                    return var.get('tempDataView').callprop('getFloat32', Js(0.0))
                PyJsHoisted_readFloat16_.func_name = 'readFloat16'
                var.put('readFloat16', PyJsHoisted_readFloat16_)
                @Js
                def PyJsHoisted_readFloat32_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    return var.get('read')(var.get('dataView').callprop('getFloat32', var.get('offset')), Js(4.0))
                PyJsHoisted_readFloat32_.func_name = 'readFloat32'
                var.put('readFloat32', PyJsHoisted_readFloat32_)
                @Js
                def PyJsHoisted_readFloat64_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    return var.get('read')(var.get('dataView').callprop('getFloat64', var.get('offset')), Js(8.0))
                PyJsHoisted_readFloat64_.func_name = 'readFloat64'
                var.put('readFloat64', PyJsHoisted_readFloat64_)
                @Js
                def PyJsHoisted_readUint8_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    return var.get('read')(var.get('dataView').callprop('getUint8', var.get('offset')), Js(1.0))
                PyJsHoisted_readUint8_.func_name = 'readUint8'
                var.put('readUint8', PyJsHoisted_readUint8_)
                @Js
                def PyJsHoisted_readUint16_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    return var.get('read')(var.get('dataView').callprop('getUint16', var.get('offset')), Js(2.0))
                PyJsHoisted_readUint16_.func_name = 'readUint16'
                var.put('readUint16', PyJsHoisted_readUint16_)
                @Js
                def PyJsHoisted_readUint32_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    return var.get('read')(var.get('dataView').callprop('getUint32', var.get('offset')), Js(4.0))
                PyJsHoisted_readUint32_.func_name = 'readUint32'
                var.put('readUint32', PyJsHoisted_readUint32_)
                @Js
                def PyJsHoisted_readUint64_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    return ((var.get('readUint32')()*var.get('POW_2_32'))+var.get('readUint32')())
                PyJsHoisted_readUint64_.func_name = 'readUint64'
                var.put('readUint64', PyJsHoisted_readUint64_)
                @Js
                def PyJsHoisted_readBreak_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    if PyJsStrictNeq(var.get('dataView').callprop('getUint8', var.get('offset')),Js(255)):
                        return Js(False)
                    var.put('offset', Js(1.0), '+')
                    return Js(True)
                PyJsHoisted_readBreak_.func_name = 'readBreak'
                var.put('readBreak', PyJsHoisted_readBreak_)
                @Js
                def PyJsHoisted_readLength_(additionalInformation, this, arguments, var=var):
                    var = Scope({'additionalInformation':additionalInformation, 'this':this, 'arguments':arguments}, var)
                    var.registers(['additionalInformation'])
                    if (var.get('additionalInformation')<Js(24.0)):
                        return var.get('additionalInformation')
                    if PyJsStrictEq(var.get('additionalInformation'),Js(24.0)):
                        return var.get('readUint8')()
                    if PyJsStrictEq(var.get('additionalInformation'),Js(25.0)):
                        return var.get('readUint16')()
                    if PyJsStrictEq(var.get('additionalInformation'),Js(26.0)):
                        return var.get('readUint32')()
                    if PyJsStrictEq(var.get('additionalInformation'),Js(27.0)):
                        return var.get('readUint64')()
                    if PyJsStrictEq(var.get('additionalInformation'),Js(31.0)):
                        return (-Js(1.0))
                    PyJsTempException = JsToPyException(Js('Invalid length encoding'))
                    raise PyJsTempException
                PyJsHoisted_readLength_.func_name = 'readLength'
                var.put('readLength', PyJsHoisted_readLength_)
                @Js
                def PyJsHoisted_readIndefiniteStringLength_(majorType, this, arguments, var=var):
                    var = Scope({'majorType':majorType, 'this':this, 'arguments':arguments}, var)
                    var.registers(['majorType', 'initialByte', 'length'])
                    var.put('initialByte', var.get('readUint8')())
                    if PyJsStrictEq(var.get('initialByte'),Js(255)):
                        return (-Js(1.0))
                    var.put('length', var.get('readLength')((var.get('initialByte')&Js(31))))
                    if ((var.get('length')<Js(0.0)) or PyJsStrictNeq((var.get('initialByte')>>Js(5.0)),var.get('majorType'))):
                        PyJsTempException = JsToPyException(Js('Invalid indefinite length element'))
                        raise PyJsTempException
                    return var.get('length')
                PyJsHoisted_readIndefiniteStringLength_.func_name = 'readIndefiniteStringLength'
                var.put('readIndefiniteStringLength', PyJsHoisted_readIndefiniteStringLength_)
                @Js
                def PyJsHoisted_appendUtf16data_(utf16data, length, this, arguments, var=var):
                    var = Scope({'utf16data':utf16data, 'length':length, 'this':this, 'arguments':arguments}, var)
                    var.registers(['utf16data', 'value', 'i', 'length'])
                    #for JS loop
                    var.put('i', Js(0.0))
                    while (var.get('i')<var.get('length')):
                        try:
                            var.put('value', var.get('readUint8')())
                            if (var.get('value')&Js(128)):
                                if (var.get('value')<Js(224)):
                                    var.put('value', (((var.get('value')&Js(31))<<Js(6.0))|(var.get('readUint8')()&Js(63))))
                                    var.put('length', Js(1.0), '-')
                                else:
                                    if (var.get('value')<Js(240)):
                                        var.put('value', ((((var.get('value')&Js(15))<<Js(12.0))|((var.get('readUint8')()&Js(63))<<Js(6.0)))|(var.get('readUint8')()&Js(63))))
                                        var.put('length', Js(2.0), '-')
                                    else:
                                        var.put('value', (((((var.get('value')&Js(15))<<Js(18.0))|((var.get('readUint8')()&Js(63))<<Js(12.0)))|((var.get('readUint8')()&Js(63))<<Js(6.0)))|(var.get('readUint8')()&Js(63))))
                                        var.put('length', Js(3.0), '-')
                            if (var.get('value')<Js(65536)):
                                var.get('utf16data').callprop('push', var.get('value'))
                            else:
                                var.put('value', Js(65536), '-')
                                var.get('utf16data').callprop('push', (Js(55296)|(var.get('value')>>Js(10.0))))
                                var.get('utf16data').callprop('push', (Js(56320)|(var.get('value')&Js(1023))))
                        finally:
                                var.put('i',Js(var.get('i').to_number())+Js(1))
                PyJsHoisted_appendUtf16data_.func_name = 'appendUtf16data'
                var.put('appendUtf16data', PyJsHoisted_appendUtf16data_)
                @Js
                def PyJsHoisted_decodeItem_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers(['utf16data', 'initialByte', 'majorType', 'fullArray', 'elements', 'retObject', 'fullArrayLength', 'additionalInformation', 'retArray', 'fullArrayOffset', 'length', 'key', 'i'])
                    var.put('initialByte', var.get('readUint8')())
                    var.put('majorType', (var.get('initialByte')>>Js(5.0)))
                    var.put('additionalInformation', (var.get('initialByte')&Js(31)))
                    pass
                    pass
                    if PyJsStrictEq(var.get('majorType'),Js(7.0)):
                        while 1:
                            SWITCHED = False
                            CONDITION = (var.get('additionalInformation'))
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(25.0)):
                                SWITCHED = True
                                return var.get('readFloat16')()
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(26.0)):
                                SWITCHED = True
                                return var.get('readFloat32')()
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(27.0)):
                                SWITCHED = True
                                return var.get('readFloat64')()
                            SWITCHED = True
                            break
                    var.put('length', var.get('readLength')(var.get('additionalInformation')))
                    if ((var.get('length')<Js(0.0)) and ((var.get('majorType')<Js(2.0)) or (Js(6.0)<var.get('majorType')))):
                        PyJsTempException = JsToPyException(Js('Invalid length'))
                        raise PyJsTempException
                    while 1:
                        SWITCHED = False
                        CONDITION = (var.get('majorType'))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                            SWITCHED = True
                            return var.get('length')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                            SWITCHED = True
                            return ((-Js(1.0))-var.get('length'))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                            SWITCHED = True
                            if (var.get('length')<Js(0.0)):
                                var.put('elements', Js([]))
                                var.put('fullArrayLength', Js(0.0))
                                while (var.put('length', var.get('readIndefiniteStringLength')(var.get('majorType')))>=Js(0.0)):
                                    var.put('fullArrayLength', var.get('length'), '+')
                                    var.get('elements').callprop('push', var.get('readArrayBuffer')(var.get('length')))
                                var.put('fullArray', var.get('Uint8Array').create(var.get('fullArrayLength')))
                                var.put('fullArrayOffset', Js(0.0))
                                #for JS loop
                                var.put('i', Js(0.0))
                                while (var.get('i')<var.get('elements').get('length')):
                                    try:
                                        var.get('fullArray').callprop('set', var.get('elements').get(var.get('i')), var.get('fullArrayOffset'))
                                        var.put('fullArrayOffset', var.get('elements').get(var.get('i')).get('length'), '+')
                                    finally:
                                            var.put('i',Js(var.get('i').to_number())+Js(1))
                                return var.get('fullArray')
                            return var.get('readArrayBuffer')(var.get('length'))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                            SWITCHED = True
                            var.put('utf16data', Js([]))
                            if (var.get('length')<Js(0.0)):
                                while (var.put('length', var.get('readIndefiniteStringLength')(var.get('majorType')))>=Js(0.0)):
                                    var.get('appendUtf16data')(var.get('utf16data'), var.get('length'))
                            else:
                                var.get('appendUtf16data')(var.get('utf16data'), var.get('length'))
                            return var.get('String').get('fromCharCode').callprop('apply', var.get(u"null"), var.get('utf16data'))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                            SWITCHED = True
                            pass
                            if (var.get('length')<Js(0.0)):
                                var.put('retArray', Js([]))
                                while var.get('readBreak')().neg():
                                    var.get('retArray').callprop('push', var.get('decodeItem')())
                            else:
                                var.put('retArray', var.get('Array').create(var.get('length')))
                                #for JS loop
                                var.put('i', Js(0.0))
                                while (var.get('i')<var.get('length')):
                                    try:
                                        var.get('retArray').put(var.get('i'), var.get('decodeItem')())
                                    finally:
                                            var.put('i',Js(var.get('i').to_number())+Js(1))
                            return var.get('retArray')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                            SWITCHED = True
                            var.put('retObject', Js({}))
                            #for JS loop
                            var.put('i', Js(0.0))
                            while ((var.get('i')<var.get('length')) or ((var.get('length')<Js(0.0)) and var.get('readBreak')().neg())):
                                try:
                                    var.put('key', var.get('decodeItem')())
                                    var.get('retObject').put(var.get('key'), var.get('decodeItem')())
                                finally:
                                        var.put('i',Js(var.get('i').to_number())+Js(1))
                            return var.get('retObject')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                            SWITCHED = True
                            return var.get('tagger')(var.get('decodeItem')(), var.get('length'))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                            SWITCHED = True
                            while 1:
                                SWITCHED = False
                                CONDITION = (var.get('length'))
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(20.0)):
                                    SWITCHED = True
                                    return Js(False)
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(21.0)):
                                    SWITCHED = True
                                    return Js(True)
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(22.0)):
                                    SWITCHED = True
                                    return var.get(u"null")
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(23.0)):
                                    SWITCHED = True
                                    return var.get('undefined')
                                if True:
                                    SWITCHED = True
                                    return var.get('simpleValue')(var.get('length'))
                                SWITCHED = True
                                break
                        SWITCHED = True
                        break
                PyJsHoisted_decodeItem_.func_name = 'decodeItem'
                var.put('decodeItem', PyJsHoisted_decodeItem_)
                var.put('dataView', var.get('DataView').create(var.get('data')))
                var.put('offset', Js(0.0))
                if PyJsStrictNeq(var.get('tagger',throw=False).typeof(),Js('function')):
                    @Js
                    def PyJs_anonymous_2_(value, this, arguments, var=var):
                        var = Scope({'value':value, 'this':this, 'arguments':arguments}, var)
                        var.registers(['value'])
                        return var.get('value')
                    PyJs_anonymous_2_._set_name('anonymous')
                    var.put('tagger', PyJs_anonymous_2_)
                if PyJsStrictNeq(var.get('simpleValue',throw=False).typeof(),Js('function')):
                    @Js
                    def PyJs_anonymous_3_(this, arguments, var=var):
                        var = Scope({'this':this, 'arguments':arguments}, var)
                        var.registers([])
                        return var.get('undefined')
                    PyJs_anonymous_3_._set_name('anonymous')
                    var.put('simpleValue', PyJs_anonymous_3_)
                pass
                pass
                pass
                pass
                pass
                pass
                pass
                pass
                pass
                pass
                pass
                pass
                pass
                pass
                var.put('ret', var.get('decodeItem')())
                if PyJsStrictNeq(var.get('offset'),var.get('data').get('byteLength')):
                    PyJsTempException = JsToPyException(Js('Remaining bytes'))
                    raise PyJsTempException
                return var.get('ret')
            PyJsHoisted_decode_.func_name = 'decode'
            var.put('decode', PyJsHoisted_decode_)
            Js('use strict')
            var.put('POW_2_24', var.get('Math').callprop('pow', Js(2.0), (-Js(24.0))))
            var.put('POW_2_32', var.get('Math').callprop('pow', Js(2.0), Js(32.0)))
            var.put('POW_2_53', var.get('Math').callprop('pow', Js(2.0), Js(53.0)))
            pass
            pass
            var.put('obj', Js({'encode':var.get('encode'),'decode':var.get('decode')}))
            if (PyJsStrictEq(var.get('define',throw=False).typeof(),Js('function')) and var.get('define').get('amd')):
                var.get('define')(Js('cbor/cbor'), var.get('obj'))
            else:
                if (PyJsStrictNeq(var.get('module',throw=False).typeof(),Js('undefined')) and var.get('module').get('exports')):
                    var.get('module').put('exports', var.get('obj'))
                else:
                    if var.get('global').get('CBOR').neg():
                        var.get('global').put('CBOR', var.get('obj'))
        PyJs_anonymous_1_._set_name('anonymous')
        PyJs_anonymous_1_(var.get(u"this"))
    PyJs_anonymous_0_._set_name('anonymous')
    @Js
    def PyJs_anonymous_4_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['module', 'require', 'exports'])
        @Js
        def PyJs_anonymous_5_(process, setImmediate, this, arguments, var=var):
            var = Scope({'process':process, 'setImmediate':setImmediate, 'this':this, 'arguments':arguments}, var)
            var.registers(['process', 'setImmediate'])
            @Js
            def PyJs_anonymous_6_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers([])
                pass
                @Js
                def PyJs_anonymous_7_(undefined, this, arguments, var=var):
                    var = Scope({'undefined':undefined, 'this':this, 'arguments':arguments}, var)
                    var.registers(['isArray', 'reflectSupported', 'symbolsSupported', 'once', 'TargetObserver', 'objectFunctionReducer', 'undefined', 'defaultMaxListeners', 'init', 'recursivelyGarbageCollect', 'resolveOptions', 'toArray', 'constructorReducer', 'configure', 'collectTreeEvents', 'growListenerTree', 'ownKeys', 'logPossibleMemoryLeak', 'functionReducer', 'makeTypeReducer', '_global', 'makeCancelablePromise', 'EventEmitter', 'toObject', 'setupListener', '_setImmediate', 'findTargetIndex', 'setImmediateSupported', 'prototype', 'nextTickSupported', 'hasOwnProperty', 'Listener', 'searchListenerTree'])
                    @Js
                    def PyJsHoisted_init_(this, arguments, var=var):
                        var = Scope({'this':this, 'arguments':arguments}, var)
                        var.registers([])
                        var.get(u"this").put('_events', Js({}))
                        if var.get(u"this").get('_conf'):
                            var.get('configure').callprop('call', var.get(u"this"), var.get(u"this").get('_conf'))
                    PyJsHoisted_init_.func_name = 'init'
                    var.put('init', PyJsHoisted_init_)
                    @Js
                    def PyJsHoisted_configure_(conf, this, arguments, var=var):
                        var = Scope({'conf':conf, 'this':this, 'arguments':arguments}, var)
                        var.registers(['conf'])
                        if var.get('conf'):
                            var.get(u"this").put('_conf', var.get('conf'))
                            (var.get('conf').get('delimiter') and var.get(u"this").put('delimiter', var.get('conf').get('delimiter')))
                            if PyJsStrictNeq(var.get('conf').get('maxListeners'),var.get('undefined')):
                                var.get(u"this").put('_maxListeners', var.get('conf').get('maxListeners'))
                            (var.get('conf').get('wildcard') and var.get(u"this").put('wildcard', var.get('conf').get('wildcard')))
                            (var.get('conf').get('newListener') and var.get(u"this").put('_newListener', var.get('conf').get('newListener')))
                            (var.get('conf').get('removeListener') and var.get(u"this").put('_removeListener', var.get('conf').get('removeListener')))
                            (var.get('conf').get('verboseMemoryLeak') and var.get(u"this").put('verboseMemoryLeak', var.get('conf').get('verboseMemoryLeak')))
                            (var.get('conf').get('ignoreErrors') and var.get(u"this").put('ignoreErrors', var.get('conf').get('ignoreErrors')))
                            if var.get(u"this").get('wildcard'):
                                var.get(u"this").put('listenerTree', Js({}))
                    PyJsHoisted_configure_.func_name = 'configure'
                    var.put('configure', PyJsHoisted_configure_)
                    @Js
                    def PyJsHoisted_logPossibleMemoryLeak_(count, eventName, this, arguments, var=var):
                        var = Scope({'count':count, 'eventName':eventName, 'this':this, 'arguments':arguments}, var)
                        var.registers(['errorMsg', 'count', 'e', 'eventName'])
                        var.put('errorMsg', ((((Js('(node) warning: possible EventEmitter memory ')+Js('leak detected. '))+var.get('count'))+Js(' listeners added. '))+Js('Use emitter.setMaxListeners() to increase limit.')))
                        if var.get(u"this").get('verboseMemoryLeak'):
                            var.put('errorMsg', ((Js(' Event name: ')+var.get('eventName'))+Js('.')), '+')
                        if (PyJsStrictNeq(var.get('process',throw=False).typeof(),Js('undefined')) and var.get('process').get('emitWarning')):
                            var.put('e', var.get('Error').create(var.get('errorMsg')))
                            var.get('e').put('name', Js('MaxListenersExceededWarning'))
                            var.get('e').put('emitter', var.get(u"this"))
                            var.get('e').put('count', var.get('count'))
                            var.get('process').callprop('emitWarning', var.get('e'))
                        else:
                            var.get('console').callprop('error', var.get('errorMsg'))
                            if var.get('console').get('trace'):
                                var.get('console').callprop('trace')
                    PyJsHoisted_logPossibleMemoryLeak_.func_name = 'logPossibleMemoryLeak'
                    var.put('logPossibleMemoryLeak', PyJsHoisted_logPossibleMemoryLeak_)
                    @Js
                    def PyJsHoisted_toObject_(keys, values, this, arguments, var=var):
                        var = Scope({'keys':keys, 'values':values, 'this':this, 'arguments':arguments}, var)
                        var.registers(['values', 'len', 'obj', 'valuesCount', 'key', 'keys', 'i'])
                        var.put('obj', Js({}))
                        pass
                        var.put('len', var.get('keys').get('length'))
                        var.put('valuesCount', (var.get('value').get('length') if var.get('values') else Js(0.0)))
                        #for JS loop
                        var.put('i', Js(0.0))
                        while (var.get('i')<var.get('len')):
                            try:
                                var.put('key', var.get('keys').get(var.get('i')))
                                var.get('obj').put(var.get('key'), (var.get('values').get(var.get('i')) if (var.get('i')<var.get('valuesCount')) else var.get('undefined')))
                            finally:
                                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                        return var.get('obj')
                    PyJsHoisted_toObject_.func_name = 'toObject'
                    var.put('toObject', PyJsHoisted_toObject_)
                    @Js
                    def PyJsHoisted_TargetObserver_(emitter, target, options, this, arguments, var=var):
                        var = Scope({'emitter':emitter, 'target':target, 'options':options, 'this':this, 'arguments':arguments}, var)
                        var.registers(['target', 'off', 'options', 'emitter', '_observers', 'on'])
                        var.get(u"this").put('_emitter', var.get('emitter'))
                        var.get(u"this").put('_target', var.get('target'))
                        var.get(u"this").put('_listeners', Js({}))
                        var.get(u"this").put('_listenersCount', Js(0.0))
                        pass
                        if (var.get('options').get('on') or var.get('options').get('off')):
                            var.put('on', var.get('options').get('on'))
                            var.put('off', var.get('options').get('off'))
                        if var.get('target').get('addEventListener'):
                            var.put('on', var.get('target').get('addEventListener'))
                            var.put('off', var.get('target').get('removeEventListener'))
                        else:
                            if var.get('target').get('addListener'):
                                var.put('on', var.get('target').get('addListener'))
                                var.put('off', var.get('target').get('removeListener'))
                            else:
                                if var.get('target').get('on'):
                                    var.put('on', var.get('target').get('on'))
                                    var.put('off', var.get('target').get('off'))
                        if (var.get('on').neg() and var.get('off').neg()):
                            PyJsTempException = JsToPyException(var.get('Error')(Js('target does not implement any known event API')))
                            raise PyJsTempException
                        if PyJsStrictNeq(var.get('on',throw=False).typeof(),Js('function')):
                            PyJsTempException = JsToPyException(var.get('TypeError')(Js('on method must be a function')))
                            raise PyJsTempException
                        if PyJsStrictNeq(var.get('off',throw=False).typeof(),Js('function')):
                            PyJsTempException = JsToPyException(var.get('TypeError')(Js('off method must be a function')))
                            raise PyJsTempException
                        var.get(u"this").put('_on', var.get('on'))
                        var.get(u"this").put('_off', var.get('off'))
                        var.put('_observers', var.get('emitter').get('_observers'))
                        if var.get('_observers'):
                            var.get('_observers').callprop('push', var.get(u"this"))
                        else:
                            var.get('emitter').put('_observers', Js([var.get(u"this")]))
                    PyJsHoisted_TargetObserver_.func_name = 'TargetObserver'
                    var.put('TargetObserver', PyJsHoisted_TargetObserver_)
                    @Js
                    def PyJsHoisted_resolveOptions_(options, schema, reducers, allowUnknown, this, arguments, var=var):
                        var = Scope({'options':options, 'schema':schema, 'reducers':reducers, 'allowUnknown':allowUnknown, 'this':this, 'arguments':arguments}, var)
                        var.registers(['reducer', 'options', 'schema', 'computedOptions', 'length', 'reject', 'reducers', 'keys', 'value', 'allowUnknown', 'i', 'option'])
                        @Js
                        def PyJsHoisted_reject_(reason, this, arguments, var=var):
                            var = Scope({'reason':reason, 'this':this, 'arguments':arguments}, var)
                            var.registers(['reason'])
                            PyJsTempException = JsToPyException(var.get('Error')((((Js('Invalid "')+var.get('option'))+Js('" option value'))+((Js('. Reason: ')+var.get('reason')) if var.get('reason') else Js('')))))
                            raise PyJsTempException
                        PyJsHoisted_reject_.func_name = 'reject'
                        var.put('reject', PyJsHoisted_reject_)
                        var.put('computedOptions', var.get('Object').callprop('assign', Js({}), var.get('schema')))
                        if var.get('options').neg():
                            return var.get('computedOptions')
                        if PyJsStrictNeq(var.get('options',throw=False).typeof(),Js('object')):
                            PyJsTempException = JsToPyException(var.get('TypeError')(Js('options must be an object')))
                            raise PyJsTempException
                        var.put('keys', var.get('Object').callprop('keys', var.get('options')))
                        var.put('length', var.get('keys').get('length'))
                        pass
                        pass
                        pass
                        #for JS loop
                        var.put('i', Js(0.0))
                        while (var.get('i')<var.get('length')):
                            try:
                                var.put('option', var.get('keys').get(var.get('i')))
                                if (var.get('allowUnknown').neg() and var.get('hasOwnProperty').callprop('call', var.get('schema'), var.get('option')).neg()):
                                    PyJsTempException = JsToPyException(var.get('Error')(((Js('Unknown "')+var.get('option'))+Js('" option'))))
                                    raise PyJsTempException
                                var.put('value', var.get('options').get(var.get('option')))
                                if PyJsStrictNeq(var.get('value'),var.get('undefined')):
                                    var.put('reducer', var.get('reducers').get(var.get('option')))
                                    var.get('computedOptions').put(var.get('option'), (var.get('reducer')(var.get('value'), var.get('reject')) if var.get('reducer') else var.get('value')))
                            finally:
                                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                        return var.get('computedOptions')
                    PyJsHoisted_resolveOptions_.func_name = 'resolveOptions'
                    var.put('resolveOptions', PyJsHoisted_resolveOptions_)
                    @Js
                    def PyJsHoisted_constructorReducer_(value, reject, this, arguments, var=var):
                        var = Scope({'value':value, 'reject':reject, 'this':this, 'arguments':arguments}, var)
                        var.registers(['value', 'reject'])
                        if (PyJsStrictNeq(var.get('value',throw=False).typeof(),Js('function')) or var.get('value').callprop('hasOwnProperty', Js('prototype')).neg()):
                            var.get('reject')(Js('value must be a constructor'))
                        return var.get('value')
                    PyJsHoisted_constructorReducer_.func_name = 'constructorReducer'
                    var.put('constructorReducer', PyJsHoisted_constructorReducer_)
                    @Js
                    def PyJsHoisted_makeTypeReducer_(types, this, arguments, var=var):
                        var = Scope({'types':types, 'this':this, 'arguments':arguments}, var)
                        var.registers(['firstType', 'len', 'secondType', 'types', 'message'])
                        var.put('message', (Js('value must be type of ')+var.get('types').callprop('join', Js('|'))))
                        var.put('len', var.get('types').get('length'))
                        var.put('firstType', var.get('types').get('0'))
                        var.put('secondType', var.get('types').get('1'))
                        if PyJsStrictEq(var.get('len'),Js(1.0)):
                            @Js
                            def PyJs_anonymous_16_(v, reject, this, arguments, var=var):
                                var = Scope({'v':v, 'reject':reject, 'this':this, 'arguments':arguments}, var)
                                var.registers(['v', 'reject'])
                                if PyJsStrictEq(var.get('v',throw=False).typeof(),var.get('firstType')):
                                    return var.get('v')
                                var.get('reject')(var.get('message'))
                            PyJs_anonymous_16_._set_name('anonymous')
                            return PyJs_anonymous_16_
                        if PyJsStrictEq(var.get('len'),Js(2.0)):
                            @Js
                            def PyJs_anonymous_17_(v, reject, this, arguments, var=var):
                                var = Scope({'v':v, 'reject':reject, 'this':this, 'arguments':arguments}, var)
                                var.registers(['reject', 'v', 'kind'])
                                var.put('kind', var.get('v',throw=False).typeof())
                                if (PyJsStrictEq(var.get('kind'),var.get('firstType')) or PyJsStrictEq(var.get('kind'),var.get('secondType'))):
                                    return var.get('v')
                                var.get('reject')(var.get('message'))
                            PyJs_anonymous_17_._set_name('anonymous')
                            return PyJs_anonymous_17_
                        @Js
                        def PyJs_anonymous_18_(v, reject, this, arguments, var=var):
                            var = Scope({'v':v, 'reject':reject, 'this':this, 'arguments':arguments}, var)
                            var.registers(['reject', 'v', 'i', 'kind'])
                            var.put('kind', var.get('v',throw=False).typeof())
                            var.put('i', var.get('len'))
                            while ((var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))>Js(0.0)):
                                if PyJsStrictEq(var.get('kind'),var.get('types').get(var.get('i'))):
                                    return var.get('v')
                            var.get('reject')(var.get('message'))
                        PyJs_anonymous_18_._set_name('anonymous')
                        return PyJs_anonymous_18_
                    PyJsHoisted_makeTypeReducer_.func_name = 'makeTypeReducer'
                    var.put('makeTypeReducer', PyJsHoisted_makeTypeReducer_)
                    @Js
                    def PyJsHoisted_makeCancelablePromise_(Promise, executor, options, this, arguments, var=var):
                        var = Scope({'Promise':Promise, 'executor':executor, 'options':options, 'this':this, 'arguments':arguments}, var)
                        var.registers(['subscriptionClosed', 'callbacks', 'options', 'promise', 'isCancelable', 'executor', 'timer', 'Promise'])
                        pass
                        pass
                        var.put('timer', Js(0.0))
                        pass
                        @Js
                        def PyJs_anonymous_19_(resolve, reject, onCancel, this, arguments, var=var):
                            var = Scope({'resolve':resolve, 'reject':reject, 'onCancel':onCancel, 'this':this, 'arguments':arguments}, var)
                            var.registers(['_resolve', 'cleanup', 'resolve', 'reject', '_reject', 'onCancel'])
                            @Js
                            def PyJsHoisted_cleanup_(this, arguments, var=var):
                                var = Scope({'this':this, 'arguments':arguments}, var)
                                var.registers([])
                                if var.get('callbacks'):
                                    var.put('callbacks', var.get(u"null"))
                                if var.get('timer'):
                                    var.get('clearTimeout')(var.get('timer'))
                                    var.put('timer', Js(0.0))
                            PyJsHoisted_cleanup_.func_name = 'cleanup'
                            var.put('cleanup', PyJsHoisted_cleanup_)
                            @Js
                            def PyJs_anonymous_20_(value, reject, this, arguments, var=var):
                                var = Scope({'value':value, 'reject':reject, 'this':this, 'arguments':arguments}, var)
                                var.registers(['value', 'reject'])
                                var.put('value', Js(1.0), '*')
                                if ((PyJsStrictNeq(var.get('value',throw=False).typeof(),Js('number')) or (var.get('value')<Js(0.0))) or var.get('Number').callprop('isFinite', var.get('value')).neg()):
                                    var.get('reject')(Js('timeout must be a positive number'))
                                return var.get('value')
                            PyJs_anonymous_20_._set_name('anonymous')
                            var.put('options', var.get('resolveOptions')(var.get('options'), Js({'timeout':Js(0.0),'overload':Js(False)}), Js({'timeout':PyJs_anonymous_20_})))
                            var.put('isCancelable', ((var.get('options').get('overload').neg() and PyJsStrictEq(var.get('Promise').get('prototype').get('cancel').typeof(),Js('function'))) and PyJsStrictEq(var.get('onCancel',throw=False).typeof(),Js('function'))))
                            pass
                            @Js
                            def PyJs_anonymous_21_(value, this, arguments, var=var):
                                var = Scope({'value':value, 'this':this, 'arguments':arguments}, var)
                                var.registers(['value'])
                                var.get('cleanup')()
                                var.get('resolve')(var.get('value'))
                            PyJs_anonymous_21_._set_name('anonymous')
                            var.put('_resolve', PyJs_anonymous_21_)
                            @Js
                            def PyJs_anonymous_22_(err, this, arguments, var=var):
                                var = Scope({'err':err, 'this':this, 'arguments':arguments}, var)
                                var.registers(['err'])
                                var.get('cleanup')()
                                var.get('reject')(var.get('err'))
                            PyJs_anonymous_22_._set_name('anonymous')
                            var.put('_reject', PyJs_anonymous_22_)
                            if var.get('isCancelable'):
                                var.get('executor')(var.get('_resolve'), var.get('_reject'), var.get('onCancel'))
                            else:
                                @Js
                                def PyJs_anonymous_23_(reason, this, arguments, var=var):
                                    var = Scope({'reason':reason, 'this':this, 'arguments':arguments}, var)
                                    var.registers(['reason'])
                                    var.get('_reject')((var.get('reason') or var.get('Error')(Js('canceled'))))
                                PyJs_anonymous_23_._set_name('anonymous')
                                var.put('callbacks', Js([PyJs_anonymous_23_]))
                                @Js
                                def PyJs_anonymous_24_(cb, this, arguments, var=var):
                                    var = Scope({'cb':cb, 'this':this, 'arguments':arguments}, var)
                                    var.registers(['cb'])
                                    if var.get('subscriptionClosed'):
                                        PyJsTempException = JsToPyException(var.get('Error')(Js('Unable to subscribe on cancel event asynchronously')))
                                        raise PyJsTempException
                                    if PyJsStrictNeq(var.get('cb',throw=False).typeof(),Js('function')):
                                        PyJsTempException = JsToPyException(var.get('TypeError')(Js('onCancel callback must be a function')))
                                        raise PyJsTempException
                                    var.get('callbacks').callprop('push', var.get('cb'))
                                PyJs_anonymous_24_._set_name('anonymous')
                                var.get('executor')(var.get('_resolve'), var.get('_reject'), PyJs_anonymous_24_)
                                var.put('subscriptionClosed', Js(True))
                            if (var.get('options').get('timeout')>Js(0.0)):
                                @Js
                                def PyJs_anonymous_25_(this, arguments, var=var):
                                    var = Scope({'this':this, 'arguments':arguments}, var)
                                    var.registers(['reason'])
                                    var.put('reason', var.get('Error')(Js('timeout')))
                                    var.get('reason').put('code', Js('ETIMEDOUT'))
                                    var.put('timer', Js(0.0))
                                    var.get('promise').callprop('cancel', var.get('reason'))
                                    var.get('reject')(var.get('reason'))
                                PyJs_anonymous_25_._set_name('anonymous')
                                var.put('timer', var.get('setTimeout')(PyJs_anonymous_25_, var.get('options').get('timeout')))
                        PyJs_anonymous_19_._set_name('anonymous')
                        var.put('promise', var.get('Promise').create(PyJs_anonymous_19_))
                        if var.get('isCancelable').neg():
                            @Js
                            def PyJs_anonymous_26_(reason, this, arguments, var=var):
                                var = Scope({'reason':reason, 'this':this, 'arguments':arguments}, var)
                                var.registers(['reason', 'i', 'length'])
                                if var.get('callbacks').neg():
                                    return var.get('undefined')
                                var.put('length', var.get('callbacks').get('length'))
                                #for JS loop
                                var.put('i', Js(1.0))
                                while (var.get('i')<var.get('length')):
                                    try:
                                        var.get('callbacks').callprop(var.get('i'), var.get('reason'))
                                    finally:
                                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                                var.get('callbacks').callprop('0', var.get('reason'))
                                var.put('callbacks', var.get(u"null"))
                            PyJs_anonymous_26_._set_name('anonymous')
                            var.get('promise').put('cancel', PyJs_anonymous_26_)
                        return var.get('promise')
                    PyJsHoisted_makeCancelablePromise_.func_name = 'makeCancelablePromise'
                    var.put('makeCancelablePromise', PyJsHoisted_makeCancelablePromise_)
                    @Js
                    def PyJsHoisted_findTargetIndex_(observer, this, arguments, var=var):
                        var = Scope({'observer':observer, 'this':this, 'arguments':arguments}, var)
                        var.registers(['observers', 'observer', 'len', 'i'])
                        var.put('observers', var.get(u"this").get('_observers'))
                        if var.get('observers').neg():
                            return (-Js(1.0))
                        var.put('len', var.get('observers').get('length'))
                        #for JS loop
                        var.put('i', Js(0.0))
                        while (var.get('i')<var.get('len')):
                            try:
                                if PyJsStrictEq(var.get('observers').get(var.get('i')).get('_target'),var.get('observer')):
                                    return var.get('i')
                            finally:
                                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                        return (-Js(1.0))
                    PyJsHoisted_findTargetIndex_.func_name = 'findTargetIndex'
                    var.put('findTargetIndex', PyJsHoisted_findTargetIndex_)
                    @Js
                    def PyJsHoisted_searchListenerTree_(handlers, type, tree, i, typeLength, this, arguments, var=var):
                        var = Scope({'handlers':handlers, 'type':type, 'tree':tree, 'i':i, 'typeLength':typeLength, 'this':this, 'arguments':arguments}, var)
                        var.registers(['j', 'xxTree', 'endReached', 'branches', 'nextType', 'handlers', 'i', 'delimiter', 'currentType', 'isolatedBranch', 'typeLength', '_listeners', 'branch', 'kind', 'xTree', 'listeners', 'l', 'dl', 'n', 'type', 'tree', 'ns'])
                        if var.get('tree').neg():
                            return var.get(u"null")
                        if PyJsStrictEq(var.get('i'),Js(0.0)):
                            var.put('kind', var.get('type',throw=False).typeof())
                            if PyJsStrictEq(var.get('kind'),Js('string')):
                                var.put('l', Js(0.0))
                                var.put('j', Js(0.0))
                                var.put('delimiter', var.get(u"this").get('delimiter'))
                                var.put('dl', var.get('delimiter').get('length'))
                                if PyJsStrictNeq(var.put('n', var.get('type').callprop('indexOf', var.get('delimiter'))),(-Js(1.0))):
                                    var.put('ns', var.get('Array').create(Js(5.0)))
                                    while 1:
                                        var.get('ns').put((var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1)), var.get('type').callprop('slice', var.get('j'), var.get('n')))
                                        var.put('j', (var.get('n')+var.get('dl')))
                                        if not PyJsStrictNeq(var.put('n', var.get('type').callprop('indexOf', var.get('delimiter'), var.get('j'))),(-Js(1.0))):
                                            break
                                    var.get('ns').put((var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1)), var.get('type').callprop('slice', var.get('j')))
                                    var.put('type', var.get('ns'))
                                    var.put('typeLength', var.get('l'))
                                else:
                                    var.put('type', Js([var.get('type')]))
                                    var.put('typeLength', Js(1.0))
                            else:
                                if PyJsStrictEq(var.get('kind'),Js('object')):
                                    var.put('typeLength', var.get('type').get('length'))
                                else:
                                    var.put('type', Js([var.get('type')]))
                                    var.put('typeLength', Js(1.0))
                        var.put('listeners', var.get(u"null"))
                        var.put('currentType', var.get('type').get(var.get('i')))
                        var.put('nextType', var.get('type').get((var.get('i')+Js(1.0))))
                        if PyJsStrictEq(var.get('i'),var.get('typeLength')):
                            if var.get('tree').get('_listeners'):
                                if PyJsStrictEq(var.get('tree').get('_listeners').typeof(),Js('function')):
                                    (var.get('handlers') and var.get('handlers').callprop('push', var.get('tree').get('_listeners')))
                                    var.put('listeners', Js([var.get('tree')]))
                                else:
                                    (var.get('handlers') and var.get('handlers').get('push').callprop('apply', var.get('handlers'), var.get('tree').get('_listeners')))
                                    var.put('listeners', Js([var.get('tree')]))
                        else:
                            if PyJsStrictEq(var.get('currentType'),Js('*')):
                                var.put('branches', var.get('ownKeys')(var.get('tree')))
                                var.put('n', var.get('branches').get('length'))
                                while ((var.put('n',Js(var.get('n').to_number())-Js(1))+Js(1))>Js(0.0)):
                                    var.put('branch', var.get('branches').get(var.get('n')))
                                    if PyJsStrictNeq(var.get('branch'),Js('_listeners')):
                                        var.put('_listeners', var.get('searchListenerTree')(var.get('handlers'), var.get('type'), var.get('tree').get(var.get('branch')), (var.get('i')+Js(1.0)), var.get('typeLength')))
                                        if var.get('_listeners'):
                                            if var.get('listeners'):
                                                var.get('listeners').get('push').callprop('apply', var.get('listeners'), var.get('_listeners'))
                                            else:
                                                var.put('listeners', var.get('_listeners'))
                                return var.get('listeners')
                            else:
                                if PyJsStrictEq(var.get('currentType'),Js('**')):
                                    var.put('endReached', (PyJsStrictEq((var.get('i')+Js(1.0)),var.get('typeLength')) or (PyJsStrictEq((var.get('i')+Js(2.0)),var.get('typeLength')) and PyJsStrictEq(var.get('nextType'),Js('*')))))
                                    if (var.get('endReached') and var.get('tree').get('_listeners')):
                                        var.put('listeners', var.get('searchListenerTree')(var.get('handlers'), var.get('type'), var.get('tree'), var.get('typeLength'), var.get('typeLength')))
                                    var.put('branches', var.get('ownKeys')(var.get('tree')))
                                    var.put('n', var.get('branches').get('length'))
                                    while ((var.put('n',Js(var.get('n').to_number())-Js(1))+Js(1))>Js(0.0)):
                                        var.put('branch', var.get('branches').get(var.get('n')))
                                        if PyJsStrictNeq(var.get('branch'),Js('_listeners')):
                                            if (PyJsStrictEq(var.get('branch'),Js('*')) or PyJsStrictEq(var.get('branch'),Js('**'))):
                                                if (var.get('tree').get(var.get('branch')).get('_listeners') and var.get('endReached').neg()):
                                                    var.put('_listeners', var.get('searchListenerTree')(var.get('handlers'), var.get('type'), var.get('tree').get(var.get('branch')), var.get('typeLength'), var.get('typeLength')))
                                                    if var.get('_listeners'):
                                                        if var.get('listeners'):
                                                            var.get('listeners').get('push').callprop('apply', var.get('listeners'), var.get('_listeners'))
                                                        else:
                                                            var.put('listeners', var.get('_listeners'))
                                                var.put('_listeners', var.get('searchListenerTree')(var.get('handlers'), var.get('type'), var.get('tree').get(var.get('branch')), var.get('i'), var.get('typeLength')))
                                            else:
                                                if PyJsStrictEq(var.get('branch'),var.get('nextType')):
                                                    var.put('_listeners', var.get('searchListenerTree')(var.get('handlers'), var.get('type'), var.get('tree').get(var.get('branch')), (var.get('i')+Js(2.0)), var.get('typeLength')))
                                                else:
                                                    var.put('_listeners', var.get('searchListenerTree')(var.get('handlers'), var.get('type'), var.get('tree').get(var.get('branch')), var.get('i'), var.get('typeLength')))
                                            if var.get('_listeners'):
                                                if var.get('listeners'):
                                                    var.get('listeners').get('push').callprop('apply', var.get('listeners'), var.get('_listeners'))
                                                else:
                                                    var.put('listeners', var.get('_listeners'))
                                    return var.get('listeners')
                                else:
                                    if var.get('tree').get(var.get('currentType')):
                                        var.put('listeners', var.get('searchListenerTree')(var.get('handlers'), var.get('type'), var.get('tree').get(var.get('currentType')), (var.get('i')+Js(1.0)), var.get('typeLength')))
                        var.put('xTree', var.get('tree').get('*'))
                        if var.get('xTree'):
                            var.get('searchListenerTree')(var.get('handlers'), var.get('type'), var.get('xTree'), (var.get('i')+Js(1.0)), var.get('typeLength'))
                        var.put('xxTree', var.get('tree').get('**'))
                        if var.get('xxTree'):
                            if (var.get('i')<var.get('typeLength')):
                                if var.get('xxTree').get('_listeners'):
                                    var.get('searchListenerTree')(var.get('handlers'), var.get('type'), var.get('xxTree'), var.get('typeLength'), var.get('typeLength'))
                                var.put('branches', var.get('ownKeys')(var.get('xxTree')))
                                var.put('n', var.get('branches').get('length'))
                                while ((var.put('n',Js(var.get('n').to_number())-Js(1))+Js(1))>Js(0.0)):
                                    var.put('branch', var.get('branches').get(var.get('n')))
                                    if PyJsStrictNeq(var.get('branch'),Js('_listeners')):
                                        if PyJsStrictEq(var.get('branch'),var.get('nextType')):
                                            var.get('searchListenerTree')(var.get('handlers'), var.get('type'), var.get('xxTree').get(var.get('branch')), (var.get('i')+Js(2.0)), var.get('typeLength'))
                                        else:
                                            if PyJsStrictEq(var.get('branch'),var.get('currentType')):
                                                var.get('searchListenerTree')(var.get('handlers'), var.get('type'), var.get('xxTree').get(var.get('branch')), (var.get('i')+Js(1.0)), var.get('typeLength'))
                                            else:
                                                var.put('isolatedBranch', Js({}))
                                                var.get('isolatedBranch').put(var.get('branch'), var.get('xxTree').get(var.get('branch')))
                                                var.get('searchListenerTree')(var.get('handlers'), var.get('type'), Js({'**':var.get('isolatedBranch')}), (var.get('i')+Js(1.0)), var.get('typeLength'))
                            else:
                                if var.get('xxTree').get('_listeners'):
                                    var.get('searchListenerTree')(var.get('handlers'), var.get('type'), var.get('xxTree'), var.get('typeLength'), var.get('typeLength'))
                                else:
                                    if (var.get('xxTree').get('*') and var.get('xxTree').get('*').get('_listeners')):
                                        var.get('searchListenerTree')(var.get('handlers'), var.get('type'), var.get('xxTree').get('*'), var.get('typeLength'), var.get('typeLength'))
                        return var.get('listeners')
                    PyJsHoisted_searchListenerTree_.func_name = 'searchListenerTree'
                    var.put('searchListenerTree', PyJsHoisted_searchListenerTree_)
                    @Js
                    def PyJsHoisted_growListenerTree_(type, listener, prepend, this, arguments, var=var):
                        var = Scope({'type':type, 'listener':listener, 'prepend':prepend, 'this':this, 'arguments':arguments}, var)
                        var.registers(['j', 'prepend', 'listener', 'len', 'dl', 'ns', 'type', 'name', 'tree', 'i', 'delimiter'])
                        var.put('len', Js(0.0))
                        var.put('j', Js(0.0))
                        var.put('delimiter', var.get(u"this").get('delimiter'))
                        var.put('dl', var.get('delimiter').get('length'))
                        if PyJsStrictEq(var.get('type',throw=False).typeof(),Js('string')):
                            if PyJsStrictNeq(var.put('i', var.get('type').callprop('indexOf', var.get('delimiter'))),(-Js(1.0))):
                                var.put('ns', var.get('Array').create(Js(5.0)))
                                while 1:
                                    var.get('ns').put((var.put('len',Js(var.get('len').to_number())+Js(1))-Js(1)), var.get('type').callprop('slice', var.get('j'), var.get('i')))
                                    var.put('j', (var.get('i')+var.get('dl')))
                                    if not PyJsStrictNeq(var.put('i', var.get('type').callprop('indexOf', var.get('delimiter'), var.get('j'))),(-Js(1.0))):
                                        break
                                var.get('ns').put((var.put('len',Js(var.get('len').to_number())+Js(1))-Js(1)), var.get('type').callprop('slice', var.get('j')))
                            else:
                                var.put('ns', Js([var.get('type')]))
                                var.put('len', Js(1.0))
                        else:
                            var.put('ns', var.get('type'))
                            var.put('len', var.get('type').get('length'))
                        if (var.get('len')>Js(1.0)):
                            #for JS loop
                            var.put('i', Js(0.0))
                            while ((var.get('i')+Js(1.0))<var.get('len')):
                                try:
                                    if (PyJsStrictEq(var.get('ns').get(var.get('i')),Js('**')) and PyJsStrictEq(var.get('ns').get((var.get('i')+Js(1.0))),Js('**'))):
                                        return var.get('undefined')
                                finally:
                                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                        var.put('tree', var.get(u"this").get('listenerTree'))
                        #for JS loop
                        var.put('i', Js(0.0))
                        while (var.get('i')<var.get('len')):
                            try:
                                var.put('name', var.get('ns').get(var.get('i')))
                                var.put('tree', (var.get('tree').get(var.get('name')) or var.get('tree').put(var.get('name'), Js({}))))
                                if PyJsStrictEq(var.get('i'),(var.get('len')-Js(1.0))):
                                    if var.get('tree').get('_listeners').neg():
                                        var.get('tree').put('_listeners', var.get('listener'))
                                    else:
                                        if PyJsStrictEq(var.get('tree').get('_listeners').typeof(),Js('function')):
                                            var.get('tree').put('_listeners', Js([var.get('tree').get('_listeners')]))
                                        if var.get('prepend'):
                                            var.get('tree').get('_listeners').callprop('unshift', var.get('listener'))
                                        else:
                                            var.get('tree').get('_listeners').callprop('push', var.get('listener'))
                                        if ((var.get('tree').get('_listeners').get('warned').neg() and (var.get(u"this").get('_maxListeners')>Js(0.0))) and (var.get('tree').get('_listeners').get('length')>var.get(u"this").get('_maxListeners'))):
                                            var.get('tree').get('_listeners').put('warned', Js(True))
                                            var.get('logPossibleMemoryLeak').callprop('call', var.get(u"this"), var.get('tree').get('_listeners').get('length'), var.get('name'))
                                    return Js(True)
                            finally:
                                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                        return Js(True)
                    PyJsHoisted_growListenerTree_.func_name = 'growListenerTree'
                    var.put('growListenerTree', PyJsHoisted_growListenerTree_)
                    @Js
                    def PyJsHoisted_collectTreeEvents_(tree, events, root, asArray, this, arguments, var=var):
                        var = Scope({'tree':tree, 'events':events, 'root':root, 'asArray':asArray, 'this':this, 'arguments':arguments}, var)
                        var.registers(['tree', 'path', 'root', 'hasListeners', 'events', 'branches', 'branch', 'isArrayPath', 'branchName', 'i', 'asArray'])
                        var.put('branches', var.get('ownKeys')(var.get('tree')))
                        var.put('i', var.get('branches').get('length'))
                        pass
                        var.put('hasListeners', var.get('tree').get('_listeners'))
                        pass
                        while ((var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))>Js(0.0)):
                            var.put('branchName', var.get('branches').get(var.get('i')))
                            var.put('branch', var.get('tree').get(var.get('branchName')))
                            if PyJsStrictEq(var.get('branchName'),Js('_listeners')):
                                var.put('path', var.get('root'))
                            else:
                                var.put('path', (var.get('root').callprop('concat', var.get('branchName')) if var.get('root') else Js([var.get('branchName')])))
                            var.put('isArrayPath', (var.get('asArray') or PyJsStrictEq(var.get('branchName',throw=False).typeof(),Js('symbol'))))
                            (var.get('hasListeners') and var.get('events').callprop('push', (var.get('path') if var.get('isArrayPath') else var.get('path').callprop('join', var.get(u"this").get('delimiter')))))
                            if PyJsStrictEq(var.get('branch',throw=False).typeof(),Js('object')):
                                var.get('collectTreeEvents').callprop('call', var.get(u"this"), var.get('branch'), var.get('events'), var.get('path'), var.get('isArrayPath'))
                        return var.get('events')
                    PyJsHoisted_collectTreeEvents_.func_name = 'collectTreeEvents'
                    var.put('collectTreeEvents', PyJsHoisted_collectTreeEvents_)
                    @Js
                    def PyJsHoisted_recursivelyGarbageCollect_(root, this, arguments, var=var):
                        var = Scope({'root':root, 'this':this, 'arguments':arguments}, var)
                        var.registers(['root', 'obj', 'flag', 'key', 'keys', 'i'])
                        var.put('keys', var.get('ownKeys')(var.get('root')))
                        var.put('i', var.get('keys').get('length'))
                        pass
                        while ((var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))>Js(0.0)):
                            var.put('key', var.get('keys').get(var.get('i')))
                            var.put('obj', var.get('root').get(var.get('key')))
                            if var.get('obj'):
                                var.put('flag', Js(True))
                                if (PyJsStrictNeq(var.get('key'),Js('_listeners')) and var.get('recursivelyGarbageCollect')(var.get('obj')).neg()):
                                    var.get('root').delete(var.get('key'))
                        return var.get('flag')
                    PyJsHoisted_recursivelyGarbageCollect_.func_name = 'recursivelyGarbageCollect'
                    var.put('recursivelyGarbageCollect', PyJsHoisted_recursivelyGarbageCollect_)
                    @Js
                    def PyJsHoisted_Listener_(emitter, event, listener, this, arguments, var=var):
                        var = Scope({'emitter':emitter, 'event':event, 'listener':listener, 'this':this, 'arguments':arguments}, var)
                        var.registers(['event', 'listener', 'emitter'])
                        var.get(u"this").put('emitter', var.get('emitter'))
                        var.get(u"this").put('event', var.get('event'))
                        var.get(u"this").put('listener', var.get('listener'))
                    PyJsHoisted_Listener_.func_name = 'Listener'
                    var.put('Listener', PyJsHoisted_Listener_)
                    @Js
                    def PyJsHoisted_setupListener_(event, listener, options, this, arguments, var=var):
                        var = Scope({'event':event, 'listener':listener, 'options':options, 'this':this, 'arguments':arguments}, var)
                        var.registers(['event', 'options', 'listener', 'objectify', '_origin', 'nextTick', '_listener', 'async', 'promisify'])
                        if PyJsStrictEq(var.get('options'),Js(True)):
                            var.put('promisify', Js(True))
                        else:
                            if PyJsStrictEq(var.get('options'),Js(False)):
                                var.put('async', Js(True))
                            else:
                                if (var.get('options').neg() or PyJsStrictNeq(var.get('options',throw=False).typeof(),Js('object'))):
                                    PyJsTempException = JsToPyException(var.get('TypeError')(Js('options should be an object or true')))
                                    raise PyJsTempException
                                var.put('async', var.get('options').get('async'))
                                var.put('promisify', var.get('options').get('promisify'))
                                var.put('nextTick', var.get('options').get('nextTick'))
                                var.put('objectify', var.get('options').get('objectify'))
                        if ((var.get('async') or var.get('nextTick')) or var.get('promisify')):
                            var.put('_listener', var.get('listener'))
                            var.put('_origin', (var.get('listener').get('_origin') or var.get('listener')))
                            if (var.get('nextTick') and var.get('nextTickSupported').neg()):
                                PyJsTempException = JsToPyException(var.get('Error')(Js('process.nextTick is not supported')))
                                raise PyJsTempException
                            if PyJsStrictEq(var.get('promisify'),var.get('undefined')):
                                var.put('promisify', PyJsStrictEq(var.get('listener').get('constructor').get('name'),Js('AsyncFunction')))
                            @Js
                            def PyJs_anonymous_28_(this, arguments, var=var):
                                var = Scope({'this':this, 'arguments':arguments}, var)
                                var.registers(['event', 'args', 'context'])
                                var.put('args', var.get('arguments'))
                                var.put('context', var.get(u"this"))
                                var.put('event', var.get(u"this").get('event'))
                                @Js
                                def PyJs_anonymous_29_(this, arguments, var=var):
                                    var = Scope({'this':this, 'arguments':arguments}, var)
                                    var.registers([])
                                    var.get('context').put('event', var.get('event'))
                                    return var.get('_listener').callprop('apply', var.get('context'), var.get('args'))
                                PyJs_anonymous_29_._set_name('anonymous')
                                @Js
                                def PyJs_anonymous_30_(resolve, this, arguments, var=var):
                                    var = Scope({'resolve':resolve, 'this':this, 'arguments':arguments}, var)
                                    var.registers(['resolve'])
                                    var.get('_setImmediate')(var.get('resolve'))
                                PyJs_anonymous_30_._set_name('anonymous')
                                @Js
                                def PyJs_anonymous_31_(this, arguments, var=var):
                                    var = Scope({'this':this, 'arguments':arguments}, var)
                                    var.registers([])
                                    var.get('context').put('event', var.get('event'))
                                    var.get('_listener').callprop('apply', var.get('context'), var.get('args'))
                                PyJs_anonymous_31_._set_name('anonymous')
                                return ((var.get('Promise').callprop('resolve') if var.get('nextTick') else var.get('Promise').create(PyJs_anonymous_30_).callprop('then', PyJs_anonymous_29_)) if var.get('promisify') else (var.get('process').get('nextTick') if var.get('nextTick') else var.get('_setImmediate'))(PyJs_anonymous_31_))
                            PyJs_anonymous_28_._set_name('anonymous')
                            var.put('listener', PyJs_anonymous_28_)
                            var.get('listener').put('_async', Js(True))
                            var.get('listener').put('_origin', var.get('_origin'))
                        return Js([var.get('listener'), (var.get('Listener').create(var.get(u"this"), var.get('event'), var.get('listener')) if var.get('objectify') else var.get(u"this"))])
                    PyJsHoisted_setupListener_.func_name = 'setupListener'
                    var.put('setupListener', PyJsHoisted_setupListener_)
                    @Js
                    def PyJsHoisted_EventEmitter_(conf, this, arguments, var=var):
                        var = Scope({'conf':conf, 'this':this, 'arguments':arguments}, var)
                        var.registers(['conf'])
                        var.get(u"this").put('_events', Js({}))
                        var.get(u"this").put('_newListener', Js(False))
                        var.get(u"this").put('_removeListener', Js(False))
                        var.get(u"this").put('verboseMemoryLeak', Js(False))
                        var.get('configure').callprop('call', var.get(u"this"), var.get('conf'))
                    PyJsHoisted_EventEmitter_.func_name = 'EventEmitter'
                    var.put('EventEmitter', PyJsHoisted_EventEmitter_)
                    @Js
                    def PyJsHoisted_once_(emitter, name, options, this, arguments, var=var):
                        var = Scope({'emitter':emitter, 'name':name, 'options':options, 'this':this, 'arguments':arguments}, var)
                        var.registers(['_Promise', 'name', 'options', 'emitter'])
                        var.put('options', var.get('resolveOptions')(var.get('options'), Js({'Promise':var.get('Promise'),'timeout':Js(0.0),'overload':Js(False)}), Js({'Promise':var.get('constructorReducer')})))
                        var.put('_Promise', var.get('options').get('Promise'))
                        @Js
                        def PyJs_anonymous_61_(resolve, reject, onCancel, this, arguments, var=var):
                            var = Scope({'resolve':resolve, 'reject':reject, 'onCancel':onCancel, 'this':this, 'arguments':arguments}, var)
                            var.registers(['resolve', 'handler', 'reject', 'onCancel', 'errorListener', 'eventListener'])
                            pass
                            if PyJsStrictEq(var.get('emitter').get('addEventListener').typeof(),Js('function')):
                                @Js
                                def PyJs_anonymous_62_(this, arguments, var=var):
                                    var = Scope({'this':this, 'arguments':arguments}, var)
                                    var.registers([])
                                    var.get('resolve')(var.get('toArray').callprop('apply', var.get(u"null"), var.get('arguments')))
                                PyJs_anonymous_62_._set_name('anonymous')
                                var.put('handler', PyJs_anonymous_62_)
                                @Js
                                def PyJs_anonymous_63_(this, arguments, var=var):
                                    var = Scope({'this':this, 'arguments':arguments}, var)
                                    var.registers([])
                                    var.get('emitter').callprop('removeEventListener', var.get('name'), var.get('handler'))
                                PyJs_anonymous_63_._set_name('anonymous')
                                var.get('onCancel')(PyJs_anonymous_63_)
                                var.get('emitter').callprop('addEventListener', var.get('name'), var.get('handler'), Js({'once':Js(True)}))
                                return var.get('undefined')
                            @Js
                            def PyJs_anonymous_64_(this, arguments, var=var):
                                var = Scope({'this':this, 'arguments':arguments}, var)
                                var.registers([])
                                (var.get('errorListener') and var.get('emitter').callprop('removeListener', Js('error'), var.get('errorListener')))
                                var.get('resolve')(var.get('toArray').callprop('apply', var.get(u"null"), var.get('arguments')))
                            PyJs_anonymous_64_._set_name('anonymous')
                            var.put('eventListener', PyJs_anonymous_64_)
                            pass
                            if PyJsStrictNeq(var.get('name'),Js('error')):
                                @Js
                                def PyJs_anonymous_65_(err, this, arguments, var=var):
                                    var = Scope({'err':err, 'this':this, 'arguments':arguments}, var)
                                    var.registers(['err'])
                                    var.get('emitter').callprop('removeListener', var.get('name'), var.get('eventListener'))
                                    var.get('reject')(var.get('err'))
                                PyJs_anonymous_65_._set_name('anonymous')
                                var.put('errorListener', PyJs_anonymous_65_)
                                var.get('emitter').callprop('once', Js('error'), var.get('errorListener'))
                            @Js
                            def PyJs_anonymous_66_(this, arguments, var=var):
                                var = Scope({'this':this, 'arguments':arguments}, var)
                                var.registers([])
                                (var.get('errorListener') and var.get('emitter').callprop('removeListener', Js('error'), var.get('errorListener')))
                                var.get('emitter').callprop('removeListener', var.get('name'), var.get('eventListener'))
                            PyJs_anonymous_66_._set_name('anonymous')
                            var.get('onCancel')(PyJs_anonymous_66_)
                            var.get('emitter').callprop('once', var.get('name'), var.get('eventListener'))
                        PyJs_anonymous_61_._set_name('anonymous')
                        return var.get('makeCancelablePromise')(var.get('_Promise'), PyJs_anonymous_61_, Js({'timeout':var.get('options').get('timeout'),'overload':var.get('options').get('overload')}))
                    PyJsHoisted_once_.func_name = 'once'
                    var.put('once', PyJsHoisted_once_)
                    var.put('hasOwnProperty', var.get('Object').get('hasOwnProperty'))
                    @Js
                    def PyJs__isArray_8_(obj, this, arguments, var=var):
                        var = Scope({'obj':obj, 'this':this, 'arguments':arguments, '_isArray':PyJs__isArray_8_}, var)
                        var.registers(['obj'])
                        return PyJsStrictEq(var.get('Object').get('prototype').get('toString').callprop('call', var.get('obj')),Js('[object Array]'))
                    PyJs__isArray_8_._set_name('_isArray')
                    var.put('isArray', (var.get('Array').get('isArray') if var.get('Array').get('isArray') else PyJs__isArray_8_))
                    var.put('defaultMaxListeners', Js(10.0))
                    var.put('nextTickSupported', ((var.get('process',throw=False).typeof()==Js('object')) and (var.get('process').get('nextTick').typeof()==Js('function'))))
                    var.put('symbolsSupported', PyJsStrictEq(var.get('Symbol',throw=False).typeof(),Js('function')))
                    var.put('reflectSupported', PyJsStrictEq(var.get('Reflect',throw=False).typeof(),Js('object')))
                    var.put('setImmediateSupported', PyJsStrictEq(var.get('setImmediate',throw=False).typeof(),Js('function')))
                    var.put('_setImmediate', (var.get('setImmediate') if var.get('setImmediateSupported') else var.get('setTimeout')))
                    @Js
                    def PyJs_anonymous_9_(obj, this, arguments, var=var):
                        var = Scope({'obj':obj, 'this':this, 'arguments':arguments}, var)
                        var.registers(['arr', 'obj'])
                        var.put('arr', var.get('Object').callprop('getOwnPropertyNames', var.get('obj')))
                        var.get('arr').get('push').callprop('apply', var.get('arr'), var.get('Object').callprop('getOwnPropertySymbols', var.get('obj')))
                        return var.get('arr')
                    PyJs_anonymous_9_._set_name('anonymous')
                    var.put('ownKeys', ((var.get('Reflect').get('ownKeys') if (var.get('reflectSupported') and PyJsStrictEq(var.get('Reflect').get('ownKeys').typeof(),Js('function'))) else PyJs_anonymous_9_) if var.get('symbolsSupported') else var.get('Object').get('keys')))
                    pass
                    pass
                    pass
                    @Js
                    def PyJs_anonymous_10_(a, b, c, this, arguments, var=var):
                        var = Scope({'a':a, 'b':b, 'c':c, 'this':this, 'arguments':arguments}, var)
                        var.registers(['a', 'c', 'arr', 'n', 'b'])
                        var.put('n', var.get('arguments').get('length'))
                        while 1:
                            SWITCHED = False
                            CONDITION = (var.get('n'))
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                                SWITCHED = True
                                return Js([])
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                                SWITCHED = True
                                return Js([var.get('a')])
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                                SWITCHED = True
                                return Js([var.get('a'), var.get('b')])
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                                SWITCHED = True
                                return Js([var.get('a'), var.get('b'), var.get('c')])
                            if True:
                                SWITCHED = True
                                var.put('arr', var.get('Array').create(var.get('n')))
                                while (var.put('n',Js(var.get('n').to_number())-Js(1))+Js(1)):
                                    var.get('arr').put(var.get('n'), var.get('arguments').get(var.get('n')))
                                return var.get('arr')
                            SWITCHED = True
                            break
                    PyJs_anonymous_10_._set_name('anonymous')
                    var.put('toArray', PyJs_anonymous_10_)
                    pass
                    pass
                    @Js
                    def PyJs_anonymous_11_(event, localEvent, reducer, this, arguments, var=var):
                        var = Scope({'event':event, 'localEvent':localEvent, 'reducer':reducer, 'this':this, 'arguments':arguments}, var)
                        var.registers(['reducer', 'event', 'target', 'listeners', 'localEvent', 'observer', 'emitter', 'handler'])
                        var.put('observer', var.get(u"this"))
                        var.put('target', var.get(u"this").get('_target'))
                        var.put('emitter', var.get(u"this").get('_emitter'))
                        var.put('listeners', var.get(u"this").get('_listeners'))
                        @Js
                        def PyJs_anonymous_12_(this, arguments, var=var):
                            var = Scope({'this':this, 'arguments':arguments}, var)
                            var.registers(['args', 'eventObj', 'result'])
                            var.put('args', var.get('toArray').callprop('apply', var.get(u"null"), var.get('arguments')))
                            var.put('eventObj', Js({'data':var.get('args'),'name':var.get('localEvent'),'original':var.get('event')}))
                            if var.get('reducer'):
                                var.put('result', var.get('reducer').callprop('call', var.get('target'), var.get('eventObj')))
                                if PyJsStrictNeq(var.get('result'),Js(False)):
                                    var.get('emitter').get('emit').callprop('apply', var.get('emitter'), Js([var.get('eventObj').get('name')]).callprop('concat', var.get('args')))
                                return var.get('undefined')
                            var.get('emitter').get('emit').callprop('apply', var.get('emitter'), Js([var.get('localEvent')]).callprop('concat', var.get('args')))
                        PyJs_anonymous_12_._set_name('anonymous')
                        var.put('handler', PyJs_anonymous_12_)
                        if var.get('listeners').get(var.get('event')):
                            PyJsTempException = JsToPyException(var.get('Error')(((Js("Event '")+var.get('event'))+Js("' is already listening"))))
                            raise PyJsTempException
                        (var.get(u"this").put('_listenersCount',Js(var.get(u"this").get('_listenersCount').to_number())+Js(1))-Js(1))
                        if ((var.get('emitter').get('_newListener') and var.get('emitter').get('_removeListener')) and var.get('observer').get('_onNewListener').neg()):
                            @Js
                            def PyJs_anonymous_13_(_event, this, arguments, var=var):
                                var = Scope({'_event':_event, 'this':this, 'arguments':arguments}, var)
                                var.registers(['_event'])
                                if (PyJsStrictEq(var.get('_event'),var.get('localEvent')) and PyJsStrictEq(var.get('listeners').get(var.get('event')),var.get(u"null"))):
                                    var.get('listeners').put(var.get('event'), var.get('handler'))
                                    var.get('observer').get('_on').callprop('call', var.get('target'), var.get('event'), var.get('handler'))
                            PyJs_anonymous_13_._set_name('anonymous')
                            var.get(u"this").put('_onNewListener', PyJs_anonymous_13_)
                            var.get('emitter').callprop('on', Js('newListener'), var.get(u"this").get('_onNewListener'))
                            @Js
                            def PyJs_anonymous_14_(_event, this, arguments, var=var):
                                var = Scope({'_event':_event, 'this':this, 'arguments':arguments}, var)
                                var.registers(['_event'])
                                if ((PyJsStrictEq(var.get('_event'),var.get('localEvent')) and var.get('emitter').callprop('hasListeners', var.get('_event')).neg()) and var.get('listeners').get(var.get('event'))):
                                    var.get('listeners').put(var.get('event'), var.get(u"null"))
                                    var.get('observer').get('_off').callprop('call', var.get('target'), var.get('event'), var.get('handler'))
                            PyJs_anonymous_14_._set_name('anonymous')
                            var.get(u"this").put('_onRemoveListener', PyJs_anonymous_14_)
                            var.get('listeners').put(var.get('event'), var.get(u"null"))
                            var.get('emitter').callprop('on', Js('removeListener'), var.get(u"this").get('_onRemoveListener'))
                        else:
                            var.get('listeners').put(var.get('event'), var.get('handler'))
                            var.get('observer').get('_on').callprop('call', var.get('target'), var.get('event'), var.get('handler'))
                    PyJs_anonymous_11_._set_name('anonymous')
                    @Js
                    def PyJs_anonymous_15_(event, this, arguments, var=var):
                        var = Scope({'event':event, 'this':this, 'arguments':arguments}, var)
                        var.registers(['event', 'off', 'target', 'listeners', 'clearRefs', 'observer', 'emitter', 'events', 'i', 'handler'])
                        @Js
                        def PyJsHoisted_clearRefs_(this, arguments, var=var):
                            var = Scope({'this':this, 'arguments':arguments}, var)
                            var.registers(['index'])
                            if var.get('observer').get('_onNewListener'):
                                var.get('emitter').callprop('off', Js('newListener'), var.get('observer').get('_onNewListener'))
                                var.get('emitter').callprop('off', Js('removeListener'), var.get('observer').get('_onRemoveListener'))
                                var.get('observer').put('_onNewListener', var.get(u"null"))
                                var.get('observer').put('_onRemoveListener', var.get(u"null"))
                            var.put('index', var.get('findTargetIndex').callprop('call', var.get('emitter'), var.get('observer')))
                            var.get('emitter').get('_observers').callprop('splice', var.get('index'), Js(1.0))
                        PyJsHoisted_clearRefs_.func_name = 'clearRefs'
                        var.put('clearRefs', PyJsHoisted_clearRefs_)
                        var.put('observer', var.get(u"this"))
                        var.put('listeners', var.get(u"this").get('_listeners'))
                        var.put('emitter', var.get(u"this").get('_emitter'))
                        pass
                        pass
                        var.put('off', var.get(u"this").get('_off'))
                        var.put('target', var.get(u"this").get('_target'))
                        pass
                        if (var.get('event') and PyJsStrictNeq(var.get('event',throw=False).typeof(),Js('string'))):
                            PyJsTempException = JsToPyException(var.get('TypeError')(Js('event must be a string')))
                            raise PyJsTempException
                        pass
                        if var.get('event'):
                            var.put('handler', var.get('listeners').get(var.get('event')))
                            if var.get('handler').neg():
                                return var.get('undefined')
                            var.get('off').callprop('call', var.get('target'), var.get('event'), var.get('handler'))
                            var.get('listeners').delete(var.get('event'))
                            if var.get(u"this").put('_listenersCount',Js(var.get(u"this").get('_listenersCount').to_number())-Js(1)).neg():
                                var.get('clearRefs')()
                        else:
                            var.put('events', var.get('ownKeys')(var.get('listeners')))
                            var.put('i', var.get('events').get('length'))
                            while ((var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))>Js(0.0)):
                                var.put('event', var.get('events').get(var.get('i')))
                                var.get('off').callprop('call', var.get('target'), var.get('event'), var.get('listeners').get(var.get('event')))
                            var.get(u"this").put('_listeners', Js({}))
                            var.get(u"this").put('_listenersCount', Js(0.0))
                            var.get('clearRefs')()
                    PyJs_anonymous_15_._set_name('anonymous')
                    var.get('Object').callprop('assign', var.get('TargetObserver').get('prototype'), Js({'subscribe':PyJs_anonymous_11_,'unsubscribe':PyJs_anonymous_15_}))
                    pass
                    pass
                    pass
                    var.put('functionReducer', var.get('makeTypeReducer')(Js([Js('function')])))
                    var.put('objectFunctionReducer', var.get('makeTypeReducer')(Js([Js('object'), Js('function')])))
                    pass
                    pass
                    pass
                    pass
                    pass
                    pass
                    pass
                    @Js
                    def PyJs_anonymous_27_(this, arguments, var=var):
                        var = Scope({'this':this, 'arguments':arguments}, var)
                        var.registers([])
                        var.get(u"this").get('emitter').callprop('off', var.get(u"this").get('event'), var.get(u"this").get('listener'))
                        return var.get(u"this")
                    PyJs_anonymous_27_._set_name('anonymous')
                    var.get('Listener').get('prototype').put('off', PyJs_anonymous_27_)
                    pass
                    pass
                    var.get('EventEmitter').put('EventEmitter2', var.get('EventEmitter'))
                    @Js
                    def PyJs_anonymous_32_(target, events, options, this, arguments, var=var):
                        var = Scope({'target':target, 'events':events, 'options':options, 'this':this, 'arguments':arguments}, var)
                        var.registers(['target', 'options', 'emitter', 'events', 'listen'])
                        @Js
                        def PyJsHoisted_listen_(events, this, arguments, var=var):
                            var = Scope({'events':events, 'this':this, 'arguments':arguments}, var)
                            var.registers(['event', 'isSingleReducer', 'index', 'len', 'observer', 'events', 'reducers', 'keys', 'i'])
                            if PyJsStrictNeq(var.get('events',throw=False).typeof(),Js('object')):
                                PyJsTempException = JsToPyException(var.get('TypeError')(Js('events must be an object')))
                                raise PyJsTempException
                            var.put('reducers', var.get('options').get('reducers'))
                            var.put('index', var.get('findTargetIndex').callprop('call', var.get('emitter'), var.get('target')))
                            pass
                            if PyJsStrictEq(var.get('index'),(-Js(1.0))):
                                var.put('observer', var.get('TargetObserver').create(var.get('emitter'), var.get('target'), var.get('options')))
                            else:
                                var.put('observer', var.get('emitter').get('_observers').get(var.get('index')))
                            var.put('keys', var.get('ownKeys')(var.get('events')))
                            var.put('len', var.get('keys').get('length'))
                            pass
                            var.put('isSingleReducer', PyJsStrictEq(var.get('reducers',throw=False).typeof(),Js('function')))
                            #for JS loop
                            var.put('i', Js(0.0))
                            while (var.get('i')<var.get('len')):
                                try:
                                    var.put('event', var.get('keys').get(var.get('i')))
                                    var.get('observer').callprop('subscribe', var.get('event'), (var.get('events').get(var.get('event')) or var.get('event')), (var.get('reducers') if var.get('isSingleReducer') else (var.get('reducers') and var.get('reducers').get(var.get('event')))))
                                finally:
                                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                        PyJsHoisted_listen_.func_name = 'listen'
                        var.put('listen', PyJsHoisted_listen_)
                        if PyJsStrictNeq(var.get('target',throw=False).typeof(),Js('object')):
                            PyJsTempException = JsToPyException(var.get('TypeError')(Js('target musts be an object')))
                            raise PyJsTempException
                        var.put('emitter', var.get(u"this"))
                        var.put('options', var.get('resolveOptions')(var.get('options'), Js({'on':var.get('undefined'),'off':var.get('undefined'),'reducers':var.get('undefined')}), Js({'on':var.get('functionReducer'),'off':var.get('functionReducer'),'reducers':var.get('objectFunctionReducer')})))
                        pass
                        (var.get('listen')(var.get('toObject')(var.get('events'))) if var.get('isArray')(var.get('events')) else (var.get('listen')(var.get('toObject')(var.get('events').callprop('split', JsRegExp('/\\s+/')))) if PyJsStrictEq(var.get('events',throw=False).typeof(),Js('string')) else var.get('listen')(var.get('events'))))
                        return var.get(u"this")
                    PyJs_anonymous_32_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('listenTo', PyJs_anonymous_32_)
                    @Js
                    def PyJs_anonymous_33_(target, event, this, arguments, var=var):
                        var = Scope({'target':target, 'event':event, 'this':this, 'arguments':arguments}, var)
                        var.registers(['observers', 'event', 'target', 'observer', 'matched', 'i'])
                        var.put('observers', var.get(u"this").get('_observers'))
                        if var.get('observers').neg():
                            return Js(False)
                        var.put('i', var.get('observers').get('length'))
                        pass
                        var.put('matched', Js(False))
                        if (var.get('target') and PyJsStrictNeq(var.get('target',throw=False).typeof(),Js('object'))):
                            PyJsTempException = JsToPyException(var.get('TypeError')(Js('target should be an object')))
                            raise PyJsTempException
                        while ((var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))>Js(0.0)):
                            var.put('observer', var.get('observers').get(var.get('i')))
                            if (var.get('target').neg() or PyJsStrictEq(var.get('observer').get('_target'),var.get('target'))):
                                var.get('observer').callprop('unsubscribe', var.get('event'))
                                var.put('matched', Js(True))
                        return var.get('matched')
                    PyJs_anonymous_33_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('stopListeningTo', PyJs_anonymous_33_)
                    var.get('EventEmitter').get('prototype').put('delimiter', Js('.'))
                    @Js
                    def PyJs_anonymous_34_(n, this, arguments, var=var):
                        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
                        var.registers(['n'])
                        if PyJsStrictNeq(var.get('n'),var.get('undefined')):
                            var.get(u"this").put('_maxListeners', var.get('n'))
                            if var.get(u"this").get('_conf').neg():
                                var.get(u"this").put('_conf', Js({}))
                            var.get(u"this").get('_conf').put('maxListeners', var.get('n'))
                    PyJs_anonymous_34_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('setMaxListeners', PyJs_anonymous_34_)
                    @Js
                    def PyJs_anonymous_35_(this, arguments, var=var):
                        var = Scope({'this':this, 'arguments':arguments}, var)
                        var.registers([])
                        return var.get(u"this").get('_maxListeners')
                    PyJs_anonymous_35_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('getMaxListeners', PyJs_anonymous_35_)
                    var.get('EventEmitter').get('prototype').put('event', Js(''))
                    @Js
                    def PyJs_anonymous_36_(event, fn, options, this, arguments, var=var):
                        var = Scope({'event':event, 'fn':fn, 'options':options, 'this':this, 'arguments':arguments}, var)
                        var.registers(['event', 'options', 'fn'])
                        return var.get(u"this").callprop('_once', var.get('event'), var.get('fn'), Js(False), var.get('options'))
                    PyJs_anonymous_36_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('once', PyJs_anonymous_36_)
                    @Js
                    def PyJs_anonymous_37_(event, fn, options, this, arguments, var=var):
                        var = Scope({'event':event, 'fn':fn, 'options':options, 'this':this, 'arguments':arguments}, var)
                        var.registers(['event', 'options', 'fn'])
                        return var.get(u"this").callprop('_once', var.get('event'), var.get('fn'), Js(True), var.get('options'))
                    PyJs_anonymous_37_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('prependOnceListener', PyJs_anonymous_37_)
                    @Js
                    def PyJs_anonymous_38_(event, fn, prepend, options, this, arguments, var=var):
                        var = Scope({'event':event, 'fn':fn, 'prepend':prepend, 'options':options, 'this':this, 'arguments':arguments}, var)
                        var.registers(['event', 'prepend', 'options', 'fn'])
                        return var.get(u"this").callprop('_many', var.get('event'), Js(1.0), var.get('fn'), var.get('prepend'), var.get('options'))
                    PyJs_anonymous_38_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('_once', PyJs_anonymous_38_)
                    @Js
                    def PyJs_anonymous_39_(event, ttl, fn, options, this, arguments, var=var):
                        var = Scope({'event':event, 'ttl':ttl, 'fn':fn, 'options':options, 'this':this, 'arguments':arguments}, var)
                        var.registers(['event', 'ttl', 'options', 'fn'])
                        return var.get(u"this").callprop('_many', var.get('event'), var.get('ttl'), var.get('fn'), Js(False), var.get('options'))
                    PyJs_anonymous_39_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('many', PyJs_anonymous_39_)
                    @Js
                    def PyJs_anonymous_40_(event, ttl, fn, options, this, arguments, var=var):
                        var = Scope({'event':event, 'ttl':ttl, 'fn':fn, 'options':options, 'this':this, 'arguments':arguments}, var)
                        var.registers(['event', 'ttl', 'options', 'fn'])
                        return var.get(u"this").callprop('_many', var.get('event'), var.get('ttl'), var.get('fn'), Js(True), var.get('options'))
                    PyJs_anonymous_40_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('prependMany', PyJs_anonymous_40_)
                    @Js
                    def PyJs_anonymous_41_(event, ttl, fn, prepend, options, this, arguments, var=var):
                        var = Scope({'event':event, 'ttl':ttl, 'fn':fn, 'prepend':prepend, 'options':options, 'this':this, 'arguments':arguments}, var)
                        var.registers(['self', 'event', 'prepend', 'options', 'listener', 'ttl', 'fn'])
                        @Js
                        def PyJsHoisted_listener_(this, arguments, var=var):
                            var = Scope({'this':this, 'arguments':arguments}, var)
                            var.registers([])
                            if PyJsStrictEq(var.put('ttl',Js(var.get('ttl').to_number())-Js(1)),Js(0.0)):
                                var.get('self').callprop('off', var.get('event'), var.get('listener'))
                            return var.get('fn').callprop('apply', var.get(u"this"), var.get('arguments'))
                        PyJsHoisted_listener_.func_name = 'listener'
                        var.put('listener', PyJsHoisted_listener_)
                        var.put('self', var.get(u"this"))
                        if PyJsStrictNeq(var.get('fn',throw=False).typeof(),Js('function')):
                            PyJsTempException = JsToPyException(var.get('Error').create(Js('many only accepts instances of Function')))
                            raise PyJsTempException
                        pass
                        var.get('listener').put('_origin', var.get('fn'))
                        return var.get(u"this").callprop('_on', var.get('event'), var.get('listener'), var.get('prepend'), var.get('options'))
                    PyJs_anonymous_41_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('_many', PyJs_anonymous_41_)
                    @Js
                    def PyJs_anonymous_42_(this, arguments, var=var):
                        var = Scope({'this':this, 'arguments':arguments}, var)
                        var.registers(['j', 'args', 'al', 'i', 'l', 'handler', 'type', 'wildcard', 'ns', 'containsSymbol'])
                        if (var.get(u"this").get('_events').neg() and var.get(u"this").get('_all').neg()):
                            return Js(False)
                        (var.get(u"this").get('_events') or var.get('init').callprop('call', var.get(u"this")))
                        var.put('type', var.get('arguments').get('0'))
                        var.put('wildcard', var.get(u"this").get('wildcard'))
                        pass
                        if (PyJsStrictEq(var.get('type'),Js('newListener')) and var.get(u"this").get('_newListener').neg()):
                            if var.get(u"this").get('_events').get('newListener').neg():
                                return Js(False)
                        if var.get('wildcard'):
                            var.put('ns', var.get('type'))
                            if (PyJsStrictNeq(var.get('type'),Js('newListener')) and PyJsStrictNeq(var.get('type'),Js('removeListener'))):
                                if PyJsStrictEq(var.get('type',throw=False).typeof(),Js('object')):
                                    var.put('l', var.get('type').get('length'))
                                    if var.get('symbolsSupported'):
                                        #for JS loop
                                        var.put('i', Js(0.0))
                                        while (var.get('i')<var.get('l')):
                                            try:
                                                if PyJsStrictEq(var.get('type').get(var.get('i')).typeof(),Js('symbol')):
                                                    var.put('containsSymbol', Js(True))
                                                    break
                                            finally:
                                                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                                    if var.get('containsSymbol').neg():
                                        var.put('type', var.get('type').callprop('join', var.get(u"this").get('delimiter')))
                        var.put('al', var.get('arguments').get('length'))
                        pass
                        if (var.get(u"this").get('_all') and var.get(u"this").get('_all').get('length')):
                            var.put('handler', var.get(u"this").get('_all').callprop('slice'))
                            #for JS loop
                            PyJsComma(var.put('i', Js(0.0)),var.put('l', var.get('handler').get('length')))
                            while (var.get('i')<var.get('l')):
                                try:
                                    var.get(u"this").put('event', var.get('type'))
                                    while 1:
                                        SWITCHED = False
                                        CONDITION = (var.get('al'))
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                                            SWITCHED = True
                                            var.get('handler').get(var.get('i')).callprop('call', var.get(u"this"), var.get('type'))
                                            break
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                                            SWITCHED = True
                                            var.get('handler').get(var.get('i')).callprop('call', var.get(u"this"), var.get('type'), var.get('arguments').get('1'))
                                            break
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                                            SWITCHED = True
                                            var.get('handler').get(var.get('i')).callprop('call', var.get(u"this"), var.get('type'), var.get('arguments').get('1'), var.get('arguments').get('2'))
                                            break
                                        if True:
                                            SWITCHED = True
                                            var.get('handler').get(var.get('i')).callprop('apply', var.get(u"this"), var.get('arguments'))
                                        SWITCHED = True
                                        break
                                finally:
                                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                        if var.get('wildcard'):
                            var.put('handler', Js([]))
                            var.get('searchListenerTree').callprop('call', var.get(u"this"), var.get('handler'), var.get('ns'), var.get(u"this").get('listenerTree'), Js(0.0), var.get('l'))
                        else:
                            var.put('handler', var.get(u"this").get('_events').get(var.get('type')))
                            if PyJsStrictEq(var.get('handler',throw=False).typeof(),Js('function')):
                                var.get(u"this").put('event', var.get('type'))
                                while 1:
                                    SWITCHED = False
                                    CONDITION = (var.get('al'))
                                    if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                                        SWITCHED = True
                                        var.get('handler').callprop('call', var.get(u"this"))
                                        break
                                    if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                                        SWITCHED = True
                                        var.get('handler').callprop('call', var.get(u"this"), var.get('arguments').get('1'))
                                        break
                                    if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                                        SWITCHED = True
                                        var.get('handler').callprop('call', var.get(u"this"), var.get('arguments').get('1'), var.get('arguments').get('2'))
                                        break
                                    if True:
                                        SWITCHED = True
                                        var.put('args', var.get('Array').create((var.get('al')-Js(1.0))))
                                        #for JS loop
                                        var.put('j', Js(1.0))
                                        while (var.get('j')<var.get('al')):
                                            try:
                                                var.get('args').put((var.get('j')-Js(1.0)), var.get('arguments').get(var.get('j')))
                                            finally:
                                                    (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                                        var.get('handler').callprop('apply', var.get(u"this"), var.get('args'))
                                    SWITCHED = True
                                    break
                                return Js(True)
                            else:
                                if var.get('handler'):
                                    var.put('handler', var.get('handler').callprop('slice'))
                        if (var.get('handler') and var.get('handler').get('length')):
                            if (var.get('al')>Js(3.0)):
                                var.put('args', var.get('Array').create((var.get('al')-Js(1.0))))
                                #for JS loop
                                var.put('j', Js(1.0))
                                while (var.get('j')<var.get('al')):
                                    try:
                                        var.get('args').put((var.get('j')-Js(1.0)), var.get('arguments').get(var.get('j')))
                                    finally:
                                            (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                            #for JS loop
                            PyJsComma(var.put('i', Js(0.0)),var.put('l', var.get('handler').get('length')))
                            while (var.get('i')<var.get('l')):
                                try:
                                    var.get(u"this").put('event', var.get('type'))
                                    while 1:
                                        SWITCHED = False
                                        CONDITION = (var.get('al'))
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                                            SWITCHED = True
                                            var.get('handler').get(var.get('i')).callprop('call', var.get(u"this"))
                                            break
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                                            SWITCHED = True
                                            var.get('handler').get(var.get('i')).callprop('call', var.get(u"this"), var.get('arguments').get('1'))
                                            break
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                                            SWITCHED = True
                                            var.get('handler').get(var.get('i')).callprop('call', var.get(u"this"), var.get('arguments').get('1'), var.get('arguments').get('2'))
                                            break
                                        if True:
                                            SWITCHED = True
                                            var.get('handler').get(var.get('i')).callprop('apply', var.get(u"this"), var.get('args'))
                                        SWITCHED = True
                                        break
                                finally:
                                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                            return Js(True)
                        else:
                            if ((var.get(u"this").get('ignoreErrors').neg() and var.get(u"this").get('_all').neg()) and PyJsStrictEq(var.get('type'),Js('error'))):
                                if var.get('arguments').get('1').instanceof(var.get('Error')):
                                    PyJsTempException = JsToPyException(var.get('arguments').get('1'))
                                    raise PyJsTempException
                                else:
                                    PyJsTempException = JsToPyException(var.get('Error').create(Js("Uncaught, unspecified 'error' event.")))
                                    raise PyJsTempException
                        return var.get(u"this").get('_all').neg().neg()
                    PyJs_anonymous_42_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('emit', PyJs_anonymous_42_)
                    @Js
                    def PyJs_anonymous_43_(this, arguments, var=var):
                        var = Scope({'this':this, 'arguments':arguments}, var)
                        var.registers(['j', 'args', 'al', 'i', 'l', 'promises', 'type', 'ns', 'wildcard', 'containsSymbol', 'handler'])
                        if (var.get(u"this").get('_events').neg() and var.get(u"this").get('_all').neg()):
                            return Js(False)
                        (var.get(u"this").get('_events') or var.get('init').callprop('call', var.get(u"this")))
                        var.put('type', var.get('arguments').get('0'))
                        var.put('wildcard', var.get(u"this").get('wildcard'))
                        pass
                        if (PyJsStrictEq(var.get('type'),Js('newListener')) and var.get(u"this").get('_newListener').neg()):
                            if var.get(u"this").get('_events').get('newListener').neg():
                                return var.get('Promise').callprop('resolve', Js([Js(False)]))
                        if var.get('wildcard'):
                            var.put('ns', var.get('type'))
                            if (PyJsStrictNeq(var.get('type'),Js('newListener')) and PyJsStrictNeq(var.get('type'),Js('removeListener'))):
                                if PyJsStrictEq(var.get('type',throw=False).typeof(),Js('object')):
                                    var.put('l', var.get('type').get('length'))
                                    if var.get('symbolsSupported'):
                                        #for JS loop
                                        var.put('i', Js(0.0))
                                        while (var.get('i')<var.get('l')):
                                            try:
                                                if PyJsStrictEq(var.get('type').get(var.get('i')).typeof(),Js('symbol')):
                                                    var.put('containsSymbol', Js(True))
                                                    break
                                            finally:
                                                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                                    if var.get('containsSymbol').neg():
                                        var.put('type', var.get('type').callprop('join', var.get(u"this").get('delimiter')))
                        var.put('promises', Js([]))
                        var.put('al', var.get('arguments').get('length'))
                        pass
                        if var.get(u"this").get('_all'):
                            #for JS loop
                            PyJsComma(var.put('i', Js(0.0)),var.put('l', var.get(u"this").get('_all').get('length')))
                            while (var.get('i')<var.get('l')):
                                try:
                                    var.get(u"this").put('event', var.get('type'))
                                    while 1:
                                        SWITCHED = False
                                        CONDITION = (var.get('al'))
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                                            SWITCHED = True
                                            var.get('promises').callprop('push', var.get(u"this").get('_all').get(var.get('i')).callprop('call', var.get(u"this"), var.get('type')))
                                            break
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                                            SWITCHED = True
                                            var.get('promises').callprop('push', var.get(u"this").get('_all').get(var.get('i')).callprop('call', var.get(u"this"), var.get('type'), var.get('arguments').get('1')))
                                            break
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                                            SWITCHED = True
                                            var.get('promises').callprop('push', var.get(u"this").get('_all').get(var.get('i')).callprop('call', var.get(u"this"), var.get('type'), var.get('arguments').get('1'), var.get('arguments').get('2')))
                                            break
                                        if True:
                                            SWITCHED = True
                                            var.get('promises').callprop('push', var.get(u"this").get('_all').get(var.get('i')).callprop('apply', var.get(u"this"), var.get('arguments')))
                                        SWITCHED = True
                                        break
                                finally:
                                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                        if var.get('wildcard'):
                            var.put('handler', Js([]))
                            var.get('searchListenerTree').callprop('call', var.get(u"this"), var.get('handler'), var.get('ns'), var.get(u"this").get('listenerTree'), Js(0.0))
                        else:
                            var.put('handler', var.get(u"this").get('_events').get(var.get('type')))
                        if PyJsStrictEq(var.get('handler',throw=False).typeof(),Js('function')):
                            var.get(u"this").put('event', var.get('type'))
                            while 1:
                                SWITCHED = False
                                CONDITION = (var.get('al'))
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                                    SWITCHED = True
                                    var.get('promises').callprop('push', var.get('handler').callprop('call', var.get(u"this")))
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                                    SWITCHED = True
                                    var.get('promises').callprop('push', var.get('handler').callprop('call', var.get(u"this"), var.get('arguments').get('1')))
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                                    SWITCHED = True
                                    var.get('promises').callprop('push', var.get('handler').callprop('call', var.get(u"this"), var.get('arguments').get('1'), var.get('arguments').get('2')))
                                    break
                                if True:
                                    SWITCHED = True
                                    var.put('args', var.get('Array').create((var.get('al')-Js(1.0))))
                                    #for JS loop
                                    var.put('j', Js(1.0))
                                    while (var.get('j')<var.get('al')):
                                        try:
                                            var.get('args').put((var.get('j')-Js(1.0)), var.get('arguments').get(var.get('j')))
                                        finally:
                                                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                                    var.get('promises').callprop('push', var.get('handler').callprop('apply', var.get(u"this"), var.get('args')))
                                SWITCHED = True
                                break
                        else:
                            if (var.get('handler') and var.get('handler').get('length')):
                                var.put('handler', var.get('handler').callprop('slice'))
                                if (var.get('al')>Js(3.0)):
                                    var.put('args', var.get('Array').create((var.get('al')-Js(1.0))))
                                    #for JS loop
                                    var.put('j', Js(1.0))
                                    while (var.get('j')<var.get('al')):
                                        try:
                                            var.get('args').put((var.get('j')-Js(1.0)), var.get('arguments').get(var.get('j')))
                                        finally:
                                                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                                #for JS loop
                                PyJsComma(var.put('i', Js(0.0)),var.put('l', var.get('handler').get('length')))
                                while (var.get('i')<var.get('l')):
                                    try:
                                        var.get(u"this").put('event', var.get('type'))
                                        while 1:
                                            SWITCHED = False
                                            CONDITION = (var.get('al'))
                                            if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                                                SWITCHED = True
                                                var.get('promises').callprop('push', var.get('handler').get(var.get('i')).callprop('call', var.get(u"this")))
                                                break
                                            if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                                                SWITCHED = True
                                                var.get('promises').callprop('push', var.get('handler').get(var.get('i')).callprop('call', var.get(u"this"), var.get('arguments').get('1')))
                                                break
                                            if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                                                SWITCHED = True
                                                var.get('promises').callprop('push', var.get('handler').get(var.get('i')).callprop('call', var.get(u"this"), var.get('arguments').get('1'), var.get('arguments').get('2')))
                                                break
                                            if True:
                                                SWITCHED = True
                                                var.get('promises').callprop('push', var.get('handler').get(var.get('i')).callprop('apply', var.get(u"this"), var.get('args')))
                                            SWITCHED = True
                                            break
                                    finally:
                                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                            else:
                                if ((var.get(u"this").get('ignoreErrors').neg() and var.get(u"this").get('_all').neg()) and PyJsStrictEq(var.get('type'),Js('error'))):
                                    if var.get('arguments').get('1').instanceof(var.get('Error')):
                                        return var.get('Promise').callprop('reject', var.get('arguments').get('1'))
                                    else:
                                        return var.get('Promise').callprop('reject', Js("Uncaught, unspecified 'error' event."))
                        return var.get('Promise').callprop('all', var.get('promises'))
                    PyJs_anonymous_43_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('emitAsync', PyJs_anonymous_43_)
                    @Js
                    def PyJs_anonymous_44_(type, listener, options, this, arguments, var=var):
                        var = Scope({'type':type, 'listener':listener, 'options':options, 'this':this, 'arguments':arguments}, var)
                        var.registers(['listener', 'type', 'options'])
                        return var.get(u"this").callprop('_on', var.get('type'), var.get('listener'), Js(False), var.get('options'))
                    PyJs_anonymous_44_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('on', PyJs_anonymous_44_)
                    @Js
                    def PyJs_anonymous_45_(type, listener, options, this, arguments, var=var):
                        var = Scope({'type':type, 'listener':listener, 'options':options, 'this':this, 'arguments':arguments}, var)
                        var.registers(['listener', 'type', 'options'])
                        return var.get(u"this").callprop('_on', var.get('type'), var.get('listener'), Js(True), var.get('options'))
                    PyJs_anonymous_45_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('prependListener', PyJs_anonymous_45_)
                    @Js
                    def PyJs_anonymous_46_(fn, this, arguments, var=var):
                        var = Scope({'fn':fn, 'this':this, 'arguments':arguments}, var)
                        var.registers(['fn'])
                        return var.get(u"this").callprop('_onAny', var.get('fn'), Js(False))
                    PyJs_anonymous_46_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('onAny', PyJs_anonymous_46_)
                    @Js
                    def PyJs_anonymous_47_(fn, this, arguments, var=var):
                        var = Scope({'fn':fn, 'this':this, 'arguments':arguments}, var)
                        var.registers(['fn'])
                        return var.get(u"this").callprop('_onAny', var.get('fn'), Js(True))
                    PyJs_anonymous_47_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('prependAny', PyJs_anonymous_47_)
                    var.get('EventEmitter').get('prototype').put('addListener', var.get('EventEmitter').get('prototype').get('on'))
                    @Js
                    def PyJs_anonymous_48_(fn, prepend, this, arguments, var=var):
                        var = Scope({'fn':fn, 'prepend':prepend, 'this':this, 'arguments':arguments}, var)
                        var.registers(['prepend', 'fn'])
                        if PyJsStrictNeq(var.get('fn',throw=False).typeof(),Js('function')):
                            PyJsTempException = JsToPyException(var.get('Error').create(Js('onAny only accepts instances of Function')))
                            raise PyJsTempException
                        if var.get(u"this").get('_all').neg():
                            var.get(u"this").put('_all', Js([]))
                        if var.get('prepend'):
                            var.get(u"this").get('_all').callprop('unshift', var.get('fn'))
                        else:
                            var.get(u"this").get('_all').callprop('push', var.get('fn'))
                        return var.get(u"this")
                    PyJs_anonymous_48_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('_onAny', PyJs_anonymous_48_)
                    @Js
                    def PyJs_anonymous_49_(type, listener, prepend, options, this, arguments, var=var):
                        var = Scope({'type':type, 'listener':listener, 'prepend':prepend, 'options':options, 'this':this, 'arguments':arguments}, var)
                        var.registers(['returnValue', 'prepend', 'temp', 'options', 'listener', 'type'])
                        if PyJsStrictEq(var.get('type',throw=False).typeof(),Js('function')):
                            var.get(u"this").callprop('_onAny', var.get('type'), var.get('listener'))
                            return var.get(u"this")
                        if PyJsStrictNeq(var.get('listener',throw=False).typeof(),Js('function')):
                            PyJsTempException = JsToPyException(var.get('Error').create(Js('on only accepts instances of Function')))
                            raise PyJsTempException
                        (var.get(u"this").get('_events') or var.get('init').callprop('call', var.get(u"this")))
                        var.put('returnValue', var.get(u"this"))
                        if PyJsStrictNeq(var.get('options'),var.get('undefined')):
                            var.put('temp', var.get('setupListener').callprop('call', var.get(u"this"), var.get('type'), var.get('listener'), var.get('options')))
                            var.put('listener', var.get('temp').get('0'))
                            var.put('returnValue', var.get('temp').get('1'))
                        if var.get(u"this").get('_newListener'):
                            var.get(u"this").callprop('emit', Js('newListener'), var.get('type'), var.get('listener'))
                        if var.get(u"this").get('wildcard'):
                            var.get('growListenerTree').callprop('call', var.get(u"this"), var.get('type'), var.get('listener'), var.get('prepend'))
                            return var.get('returnValue')
                        if var.get(u"this").get('_events').get(var.get('type')).neg():
                            var.get(u"this").get('_events').put(var.get('type'), var.get('listener'))
                        else:
                            if PyJsStrictEq(var.get(u"this").get('_events').get(var.get('type')).typeof(),Js('function')):
                                var.get(u"this").get('_events').put(var.get('type'), Js([var.get(u"this").get('_events').get(var.get('type'))]))
                            if var.get('prepend'):
                                var.get(u"this").get('_events').get(var.get('type')).callprop('unshift', var.get('listener'))
                            else:
                                var.get(u"this").get('_events').get(var.get('type')).callprop('push', var.get('listener'))
                            if ((var.get(u"this").get('_events').get(var.get('type')).get('warned').neg() and (var.get(u"this").get('_maxListeners')>Js(0.0))) and (var.get(u"this").get('_events').get(var.get('type')).get('length')>var.get(u"this").get('_maxListeners'))):
                                var.get(u"this").get('_events').get(var.get('type')).put('warned', Js(True))
                                var.get('logPossibleMemoryLeak').callprop('call', var.get(u"this"), var.get(u"this").get('_events').get(var.get('type')).get('length'), var.get('type'))
                        return var.get('returnValue')
                    PyJs_anonymous_49_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('_on', PyJs_anonymous_49_)
                    @Js
                    def PyJs_anonymous_50_(type, listener, this, arguments, var=var):
                        var = Scope({'type':type, 'listener':listener, 'this':this, 'arguments':arguments}, var)
                        var.registers(['iLeaf', 'leafs', 'leaf', 'handlers', 'i', 'listener', 'position', 'type', 'length', 'ns'])
                        if PyJsStrictNeq(var.get('listener',throw=False).typeof(),Js('function')):
                            PyJsTempException = JsToPyException(var.get('Error').create(Js('removeListener only takes instances of Function')))
                            raise PyJsTempException
                        var.put('leafs', Js([]))
                        if var.get(u"this").get('wildcard'):
                            var.put('ns', (var.get('type').callprop('split', var.get(u"this").get('delimiter')) if PyJsStrictEq(var.get('type',throw=False).typeof(),Js('string')) else var.get('type').callprop('slice')))
                            var.put('leafs', var.get('searchListenerTree').callprop('call', var.get(u"this"), var.get(u"null"), var.get('ns'), var.get(u"this").get('listenerTree'), Js(0.0)))
                            if var.get('leafs').neg():
                                return var.get(u"this")
                        else:
                            if var.get(u"this").get('_events').get(var.get('type')).neg():
                                return var.get(u"this")
                            var.put('handlers', var.get(u"this").get('_events').get(var.get('type')))
                            var.get('leafs').callprop('push', Js({'_listeners':var.get('handlers')}))
                        #for JS loop
                        var.put('iLeaf', Js(0.0))
                        while (var.get('iLeaf')<var.get('leafs').get('length')):
                            try:
                                var.put('leaf', var.get('leafs').get(var.get('iLeaf')))
                                var.put('handlers', var.get('leaf').get('_listeners'))
                                if var.get('isArray')(var.get('handlers')):
                                    var.put('position', (-Js(1.0)))
                                    #for JS loop
                                    var.put('i', Js(0.0))
                                    var.put('length', var.get('handlers').get('length'))
                                    while (var.get('i')<var.get('length')):
                                        try:
                                            if ((PyJsStrictEq(var.get('handlers').get(var.get('i')),var.get('listener')) or (var.get('handlers').get(var.get('i')).get('listener') and PyJsStrictEq(var.get('handlers').get(var.get('i')).get('listener'),var.get('listener')))) or (var.get('handlers').get(var.get('i')).get('_origin') and PyJsStrictEq(var.get('handlers').get(var.get('i')).get('_origin'),var.get('listener')))):
                                                var.put('position', var.get('i'))
                                                break
                                        finally:
                                                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                                    if (var.get('position')<Js(0.0)):
                                        continue
                                    if var.get(u"this").get('wildcard'):
                                        var.get('leaf').get('_listeners').callprop('splice', var.get('position'), Js(1.0))
                                    else:
                                        var.get(u"this").get('_events').get(var.get('type')).callprop('splice', var.get('position'), Js(1.0))
                                    if PyJsStrictEq(var.get('handlers').get('length'),Js(0.0)):
                                        if var.get(u"this").get('wildcard'):
                                            var.get('leaf').delete('_listeners')
                                        else:
                                            var.get(u"this").get('_events').delete(var.get('type'))
                                    if var.get(u"this").get('_removeListener'):
                                        var.get(u"this").callprop('emit', Js('removeListener'), var.get('type'), var.get('listener'))
                                    return var.get(u"this")
                                else:
                                    if ((PyJsStrictEq(var.get('handlers'),var.get('listener')) or (var.get('handlers').get('listener') and PyJsStrictEq(var.get('handlers').get('listener'),var.get('listener')))) or (var.get('handlers').get('_origin') and PyJsStrictEq(var.get('handlers').get('_origin'),var.get('listener')))):
                                        if var.get(u"this").get('wildcard'):
                                            var.get('leaf').delete('_listeners')
                                        else:
                                            var.get(u"this").get('_events').delete(var.get('type'))
                                        if var.get(u"this").get('_removeListener'):
                                            var.get(u"this").callprop('emit', Js('removeListener'), var.get('type'), var.get('listener'))
                            finally:
                                    (var.put('iLeaf',Js(var.get('iLeaf').to_number())+Js(1))-Js(1))
                        (var.get(u"this").get('listenerTree') and var.get('recursivelyGarbageCollect')(var.get(u"this").get('listenerTree')))
                        return var.get(u"this")
                    PyJs_anonymous_50_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('off', PyJs_anonymous_50_)
                    @Js
                    def PyJs_anonymous_51_(fn, this, arguments, var=var):
                        var = Scope({'fn':fn, 'this':this, 'arguments':arguments}, var)
                        var.registers(['l', 'i', 'fns', 'fn'])
                        var.put('i', Js(0.0))
                        var.put('l', Js(0.0))
                        if ((var.get('fn') and var.get(u"this").get('_all')) and (var.get(u"this").get('_all').get('length')>Js(0.0))):
                            var.put('fns', var.get(u"this").get('_all'))
                            #for JS loop
                            PyJsComma(var.put('i', Js(0.0)),var.put('l', var.get('fns').get('length')))
                            while (var.get('i')<var.get('l')):
                                try:
                                    if PyJsStrictEq(var.get('fn'),var.get('fns').get(var.get('i'))):
                                        var.get('fns').callprop('splice', var.get('i'), Js(1.0))
                                        if var.get(u"this").get('_removeListener'):
                                            var.get(u"this").callprop('emit', Js('removeListenerAny'), var.get('fn'))
                                        return var.get(u"this")
                                finally:
                                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                        else:
                            var.put('fns', var.get(u"this").get('_all'))
                            if var.get(u"this").get('_removeListener'):
                                #for JS loop
                                PyJsComma(var.put('i', Js(0.0)),var.put('l', var.get('fns').get('length')))
                                while (var.get('i')<var.get('l')):
                                    try:
                                        var.get(u"this").callprop('emit', Js('removeListenerAny'), var.get('fns').get(var.get('i')))
                                    finally:
                                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                            var.get(u"this").put('_all', Js([]))
                        return var.get(u"this")
                    PyJs_anonymous_51_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('offAny', PyJs_anonymous_51_)
                    var.get('EventEmitter').get('prototype').put('removeListener', var.get('EventEmitter').get('prototype').get('off'))
                    @Js
                    def PyJs_anonymous_52_(type, this, arguments, var=var):
                        var = Scope({'type':type, 'this':this, 'arguments':arguments}, var)
                        var.registers(['type', 'leaf', 'leafs', 'i'])
                        if PyJsStrictEq(var.get('type'),var.get('undefined')):
                            (var.get(u"this").get('_events').neg() or var.get('init').callprop('call', var.get(u"this")))
                            return var.get(u"this")
                        if var.get(u"this").get('wildcard'):
                            var.put('leafs', var.get('searchListenerTree').callprop('call', var.get(u"this"), var.get(u"null"), var.get('type'), var.get(u"this").get('listenerTree'), Js(0.0)))
                            if var.get('leafs').neg():
                                return var.get(u"this")
                            #for JS loop
                            var.put('i', Js(0.0))
                            while (var.get('i')<var.get('leafs').get('length')):
                                try:
                                    var.put('leaf', var.get('leafs').get(var.get('i')))
                                    var.get('leaf').put('_listeners', var.get(u"null"))
                                finally:
                                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                            (var.get(u"this").get('listenerTree') and var.get('recursivelyGarbageCollect')(var.get(u"this").get('listenerTree')))
                        else:
                            if var.get(u"this").get('_events'):
                                var.get(u"this").get('_events').put(var.get('type'), var.get(u"null"))
                        return var.get(u"this")
                    PyJs_anonymous_52_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('removeAllListeners', PyJs_anonymous_52_)
                    @Js
                    def PyJs_anonymous_53_(type, this, arguments, var=var):
                        var = Scope({'type':type, 'this':this, 'arguments':arguments}, var)
                        var.registers(['allListeners', 'listeners', 'handlers', 'ns', 'type', 'keys', '_events', 'listenerTree', 'i'])
                        var.put('_events', var.get(u"this").get('_events'))
                        pass
                        pass
                        pass
                        if PyJsStrictEq(var.get('type'),var.get('undefined')):
                            if var.get(u"this").get('wildcard'):
                                PyJsTempException = JsToPyException(var.get('Error')(Js('event name required for wildcard emitter')))
                                raise PyJsTempException
                            if var.get('_events').neg():
                                return Js([])
                            var.put('keys', var.get('ownKeys')(var.get('_events')))
                            var.put('i', var.get('keys').get('length'))
                            var.put('allListeners', Js([]))
                            while ((var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))>Js(0.0)):
                                var.put('listeners', var.get('_events').get(var.get('keys').get(var.get('i'))))
                                if PyJsStrictEq(var.get('listeners',throw=False).typeof(),Js('function')):
                                    var.get('allListeners').callprop('push', var.get('listeners'))
                                else:
                                    var.get('allListeners').get('push').callprop('apply', var.get('allListeners'), var.get('listeners'))
                            return var.get('allListeners')
                        else:
                            if var.get(u"this").get('wildcard'):
                                var.put('listenerTree', var.get(u"this").get('listenerTree'))
                                if var.get('listenerTree').neg():
                                    return Js([])
                                var.put('handlers', Js([]))
                                var.put('ns', (var.get('type').callprop('split', var.get(u"this").get('delimiter')) if PyJsStrictEq(var.get('type',throw=False).typeof(),Js('string')) else var.get('type').callprop('slice')))
                                var.get('searchListenerTree').callprop('call', var.get(u"this"), var.get('handlers'), var.get('ns'), var.get('listenerTree'), Js(0.0))
                                return var.get('handlers')
                            if var.get('_events').neg():
                                return Js([])
                            var.put('listeners', var.get('_events').get(var.get('type')))
                            if var.get('listeners').neg():
                                return Js([])
                            return (Js([var.get('listeners')]) if PyJsStrictEq(var.get('listeners',throw=False).typeof(),Js('function')) else var.get('listeners'))
                    PyJs_anonymous_53_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('listeners', PyJs_anonymous_53_)
                    @Js
                    def PyJs_anonymous_54_(nsAsArray, this, arguments, var=var):
                        var = Scope({'nsAsArray':nsAsArray, 'this':this, 'arguments':arguments}, var)
                        var.registers(['nsAsArray', '_events'])
                        var.put('_events', var.get(u"this").get('_events'))
                        return (var.get('collectTreeEvents').callprop('call', var.get(u"this"), var.get(u"this").get('listenerTree'), Js([]), var.get(u"null"), var.get('nsAsArray')) if var.get(u"this").get('wildcard') else (var.get('ownKeys')(var.get('_events')) if var.get('_events') else Js([])))
                    PyJs_anonymous_54_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('eventNames', PyJs_anonymous_54_)
                    @Js
                    def PyJs_anonymous_55_(type, this, arguments, var=var):
                        var = Scope({'type':type, 'this':this, 'arguments':arguments}, var)
                        var.registers(['type'])
                        return var.get(u"this").callprop('listeners', var.get('type')).get('length')
                    PyJs_anonymous_55_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('listenerCount', PyJs_anonymous_55_)
                    @Js
                    def PyJs_anonymous_56_(type, this, arguments, var=var):
                        var = Scope({'type':type, 'this':this, 'arguments':arguments}, var)
                        var.registers(['handlers', '_all', 'type', '_events', 'ns'])
                        if var.get(u"this").get('wildcard'):
                            var.put('handlers', Js([]))
                            var.put('ns', (var.get('type').callprop('split', var.get(u"this").get('delimiter')) if PyJsStrictEq(var.get('type',throw=False).typeof(),Js('string')) else var.get('type').callprop('slice')))
                            var.get('searchListenerTree').callprop('call', var.get(u"this"), var.get('handlers'), var.get('ns'), var.get(u"this").get('listenerTree'), Js(0.0))
                            return (var.get('handlers').get('length')>Js(0.0))
                        var.put('_events', var.get(u"this").get('_events'))
                        var.put('_all', var.get(u"this").get('_all'))
                        return ((var.get('_all') and var.get('_all').get('length')) or (var.get('_events') and (var.get('ownKeys')(var.get('_events')).get('length') if PyJsStrictEq(var.get('type'),var.get('undefined')) else var.get('_events').get(var.get('type'))))).neg().neg()
                    PyJs_anonymous_56_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('hasListeners', PyJs_anonymous_56_)
                    @Js
                    def PyJs_anonymous_57_(this, arguments, var=var):
                        var = Scope({'this':this, 'arguments':arguments}, var)
                        var.registers([])
                        if var.get(u"this").get('_all'):
                            return var.get(u"this").get('_all')
                        else:
                            return Js([])
                    PyJs_anonymous_57_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('listenersAny', PyJs_anonymous_57_)
                    @Js
                    def PyJs_anonymous_58_(event, options, this, arguments, var=var):
                        var = Scope({'event':event, 'options':options, 'this':this, 'arguments':arguments}, var)
                        var.registers(['self', 'event', 'type', 'options'])
                        var.put('self', var.get(u"this"))
                        var.put('type', var.get('options',throw=False).typeof())
                        if PyJsStrictEq(var.get('type'),Js('number')):
                            var.put('options', Js({'timeout':var.get('options')}))
                        else:
                            if PyJsStrictEq(var.get('type'),Js('function')):
                                var.put('options', Js({'filter':var.get('options')}))
                        var.put('options', var.get('resolveOptions')(var.get('options'), Js({'timeout':Js(0.0),'filter':var.get('undefined'),'handleError':Js(False),'Promise':var.get('Promise'),'overload':Js(False)}), Js({'filter':var.get('functionReducer'),'Promise':var.get('constructorReducer')})))
                        @Js
                        def PyJs_anonymous_59_(resolve, reject, onCancel, this, arguments, var=var):
                            var = Scope({'resolve':resolve, 'reject':reject, 'onCancel':onCancel, 'this':this, 'arguments':arguments}, var)
                            var.registers(['resolve', 'onCancel', 'listener', 'reject'])
                            @Js
                            def PyJsHoisted_listener_(this, arguments, var=var):
                                var = Scope({'this':this, 'arguments':arguments}, var)
                                var.registers(['filter', 'err'])
                                var.put('filter', var.get('options').get('filter'))
                                if (var.get('filter') and var.get('filter').callprop('apply', var.get('self'), var.get('arguments')).neg()):
                                    return var.get('undefined')
                                var.get('self').callprop('off', var.get('event'), var.get('listener'))
                                if var.get('options').get('handleError'):
                                    var.put('err', var.get('arguments').get('0'))
                                    (var.get('reject')(var.get('err')) if var.get('err') else var.get('resolve')(var.get('toArray').callprop('apply', var.get(u"null"), var.get('arguments')).callprop('slice', Js(1.0))))
                                else:
                                    var.get('resolve')(var.get('toArray').callprop('apply', var.get(u"null"), var.get('arguments')))
                            PyJsHoisted_listener_.func_name = 'listener'
                            var.put('listener', PyJsHoisted_listener_)
                            pass
                            @Js
                            def PyJs_anonymous_60_(this, arguments, var=var):
                                var = Scope({'this':this, 'arguments':arguments}, var)
                                var.registers([])
                                var.get('self').callprop('off', var.get('event'), var.get('listener'))
                            PyJs_anonymous_60_._set_name('anonymous')
                            var.get('onCancel')(PyJs_anonymous_60_)
                            var.get('self').callprop('_on', var.get('event'), var.get('listener'), Js(False))
                        PyJs_anonymous_59_._set_name('anonymous')
                        return var.get('makeCancelablePromise')(var.get('options').get('Promise'), PyJs_anonymous_59_, Js({'timeout':var.get('options').get('timeout'),'overload':var.get('options').get('overload')}))
                    PyJs_anonymous_58_._set_name('anonymous')
                    var.get('EventEmitter').get('prototype').put('waitFor', PyJs_anonymous_58_)
                    pass
                    var.put('prototype', var.get('EventEmitter').get('prototype'))
                    @Js
                    def PyJs_anonymous_67_(this, arguments, var=var):
                        var = Scope({'this':this, 'arguments':arguments}, var)
                        var.registers([])
                        return var.get('prototype').get('_maxListeners')
                    PyJs_anonymous_67_._set_name('anonymous')
                    @Js
                    def PyJs_anonymous_68_(n, this, arguments, var=var):
                        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
                        var.registers(['n'])
                        if ((PyJsStrictNeq(var.get('n',throw=False).typeof(),Js('number')) or (var.get('n')<Js(0.0))) or var.get('Number').callprop('isNaN', var.get('n'))):
                            PyJsTempException = JsToPyException(var.get('TypeError')(Js('n must be a non-negative number')))
                            raise PyJsTempException
                        var.get('prototype').put('_maxListeners', var.get('n'))
                    PyJs_anonymous_68_._set_name('anonymous')
                    var.get('Object').callprop('defineProperties', var.get('EventEmitter'), Js({'defaultMaxListeners':Js({'get':PyJs_anonymous_67_,'set':PyJs_anonymous_68_,'enumerable':Js(True)}),'once':Js({'value':var.get('once'),'writable':Js(True),'configurable':Js(True)})}))
                    var.get('Object').callprop('defineProperties', var.get('prototype'), Js({'_maxListeners':Js({'value':var.get('defaultMaxListeners'),'writable':Js(True),'configurable':Js(True)}),'_observers':Js({'value':var.get(u"null"),'writable':Js(True),'configurable':Js(True)})}))
                    if (PyJsStrictEq(var.get('define',throw=False).typeof(),Js('function')) and var.get('define').get('amd')):
                        @Js
                        def PyJs_anonymous_69_(this, arguments, var=var):
                            var = Scope({'this':this, 'arguments':arguments}, var)
                            var.registers([])
                            return var.get('EventEmitter')
                        PyJs_anonymous_69_._set_name('anonymous')
                        var.get('define')(PyJs_anonymous_69_)
                    else:
                        if PyJsStrictEq(var.get('exports',throw=False).typeof(),Js('object')):
                            var.get('module').put('exports', var.get('EventEmitter'))
                        else:
                            var.put('_global', var.get('Function').create(Js(''), Js('return this'))())
                            var.get('_global').put('EventEmitter2', var.get('EventEmitter'))
                PyJs_anonymous_7_._set_name('anonymous')
                PyJs_anonymous_7_().neg()
            PyJs_anonymous_6_._set_name('anonymous')
            PyJs_anonymous_6_.callprop('call', var.get(u"this"))
        PyJs_anonymous_5_._set_name('anonymous')
        PyJs_anonymous_5_.callprop('call', var.get(u"this"), var.get('require')(Js('_process')), var.get('require')(Js('timers')).get('setImmediate'))
    PyJs_anonymous_4_._set_name('anonymous')
    @Js
    def PyJs_anonymous_70_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['toObject', 'propIsEnumerable', 'require', 'module', 'getOwnPropertySymbols', 'shouldUseNative', 'hasOwnProperty', 'exports'])
        @Js
        def PyJsHoisted_toObject_(val, this, arguments, var=var):
            var = Scope({'val':val, 'this':this, 'arguments':arguments}, var)
            var.registers(['val'])
            if (PyJsStrictEq(var.get('val'),var.get(u"null")) or PyJsStrictEq(var.get('val'),var.get('undefined'))):
                PyJsTempException = JsToPyException(var.get('TypeError').create(Js('Object.assign cannot be called with null or undefined')))
                raise PyJsTempException
            return var.get('Object')(var.get('val'))
        PyJsHoisted_toObject_.func_name = 'toObject'
        var.put('toObject', PyJsHoisted_toObject_)
        @Js
        def PyJsHoisted_shouldUseNative_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['test2', 'test3', 'order2', 'test1', 'i'])
            try:
                if var.get('Object').get('assign').neg():
                    return Js(False)
                var.put('test1', var.get('String').create(Js('abc')))
                var.get('test1').put('5', Js('de'))
                if PyJsStrictEq(var.get('Object').callprop('getOwnPropertyNames', var.get('test1')).get('0'),Js('5')):
                    return Js(False)
                var.put('test2', Js({}))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<Js(10.0)):
                    try:
                        var.get('test2').put((Js('_')+var.get('String').callprop('fromCharCode', var.get('i'))), var.get('i'))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                @Js
                def PyJs_anonymous_71_(n, this, arguments, var=var):
                    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
                    var.registers(['n'])
                    return var.get('test2').get(var.get('n'))
                PyJs_anonymous_71_._set_name('anonymous')
                var.put('order2', var.get('Object').callprop('getOwnPropertyNames', var.get('test2')).callprop('map', PyJs_anonymous_71_))
                if PyJsStrictNeq(var.get('order2').callprop('join', Js('')),Js('0123456789')):
                    return Js(False)
                var.put('test3', Js({}))
                @Js
                def PyJs_anonymous_72_(letter, this, arguments, var=var):
                    var = Scope({'letter':letter, 'this':this, 'arguments':arguments}, var)
                    var.registers(['letter'])
                    var.get('test3').put(var.get('letter'), var.get('letter'))
                PyJs_anonymous_72_._set_name('anonymous')
                Js('abcdefghijklmnopqrst').callprop('split', Js('')).callprop('forEach', PyJs_anonymous_72_)
                if PyJsStrictNeq(var.get('Object').callprop('keys', var.get('Object').callprop('assign', Js({}), var.get('test3'))).callprop('join', Js('')),Js('abcdefghijklmnopqrst')):
                    return Js(False)
                return Js(True)
            except PyJsException as PyJsTempException:
                PyJsHolder_657272_94674737 = var.own.get('err')
                var.force_own_put('err', PyExceptionToJs(PyJsTempException))
                try:
                    return Js(False)
                finally:
                    if PyJsHolder_657272_94674737 is not None:
                        var.own['err'] = PyJsHolder_657272_94674737
                    else:
                        del var.own['err']
                    del PyJsHolder_657272_94674737
        PyJsHoisted_shouldUseNative_.func_name = 'shouldUseNative'
        var.put('shouldUseNative', PyJsHoisted_shouldUseNative_)
        Js('use strict')
        var.put('getOwnPropertySymbols', var.get('Object').get('getOwnPropertySymbols'))
        var.put('hasOwnProperty', var.get('Object').get('prototype').get('hasOwnProperty'))
        var.put('propIsEnumerable', var.get('Object').get('prototype').get('propertyIsEnumerable'))
        pass
        pass
        @Js
        def PyJs_anonymous_73_(target, source, this, arguments, var=var):
            var = Scope({'target':target, 'source':source, 'this':this, 'arguments':arguments}, var)
            var.registers(['target', 'i', 'source', 'symbols', 'key', 'to', 'from', 's'])
            pass
            var.put('to', var.get('toObject')(var.get('target')))
            pass
            #for JS loop
            var.put('s', Js(1.0))
            while (var.get('s')<var.get('arguments').get('length')):
                try:
                    var.put('from', var.get('Object')(var.get('arguments').get(var.get('s'))))
                    for PyJsTemp in var.get('from'):
                        var.put('key', PyJsTemp)
                        if var.get('hasOwnProperty').callprop('call', var.get('from'), var.get('key')):
                            var.get('to').put(var.get('key'), var.get('from').get(var.get('key')))
                    if var.get('getOwnPropertySymbols'):
                        var.put('symbols', var.get('getOwnPropertySymbols')(var.get('from')))
                        #for JS loop
                        var.put('i', Js(0.0))
                        while (var.get('i')<var.get('symbols').get('length')):
                            try:
                                if var.get('propIsEnumerable').callprop('call', var.get('from'), var.get('symbols').get(var.get('i'))):
                                    var.get('to').put(var.get('symbols').get(var.get('i')), var.get('from').get(var.get('symbols').get(var.get('i'))))
                            finally:
                                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                finally:
                        (var.put('s',Js(var.get('s').to_number())+Js(1))-Js(1))
            return var.get('to')
        PyJs_anonymous_73_._set_name('anonymous')
        var.get('module').put('exports', (var.get('Object').get('assign') if var.get('shouldUseNative')() else PyJs_anonymous_73_))
    PyJs_anonymous_70_._set_name('anonymous')
    @Js
    def PyJs_anonymous_74_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['process', 'queueIndex', 'runTimeout', 'currentQueue', 'noop', 'defaultClearTimeout', 'cachedSetTimeout', 'cachedClearTimeout', 'defaultSetTimout', 'queue', 'draining', 'cleanUpNextTick', 'require', 'module', 'runClearTimeout', 'drainQueue', 'Item', 'exports'])
        @Js
        def PyJsHoisted_defaultSetTimout_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            PyJsTempException = JsToPyException(var.get('Error').create(Js('setTimeout has not been defined')))
            raise PyJsTempException
        PyJsHoisted_defaultSetTimout_.func_name = 'defaultSetTimout'
        var.put('defaultSetTimout', PyJsHoisted_defaultSetTimout_)
        @Js
        def PyJsHoisted_defaultClearTimeout_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            PyJsTempException = JsToPyException(var.get('Error').create(Js('clearTimeout has not been defined')))
            raise PyJsTempException
        PyJsHoisted_defaultClearTimeout_.func_name = 'defaultClearTimeout'
        var.put('defaultClearTimeout', PyJsHoisted_defaultClearTimeout_)
        @Js
        def PyJsHoisted_runTimeout_(fun, this, arguments, var=var):
            var = Scope({'fun':fun, 'this':this, 'arguments':arguments}, var)
            var.registers(['fun'])
            if PyJsStrictEq(var.get('cachedSetTimeout'),var.get('setTimeout')):
                return var.get('setTimeout')(var.get('fun'), Js(0.0))
            if ((PyJsStrictEq(var.get('cachedSetTimeout'),var.get('defaultSetTimout')) or var.get('cachedSetTimeout').neg()) and var.get('setTimeout')):
                var.put('cachedSetTimeout', var.get('setTimeout'))
                return var.get('setTimeout')(var.get('fun'), Js(0.0))
            try:
                return var.get('cachedSetTimeout')(var.get('fun'), Js(0.0))
            except PyJsException as PyJsTempException:
                PyJsHolder_65_44332318 = var.own.get('e')
                var.force_own_put('e', PyExceptionToJs(PyJsTempException))
                try:
                    try:
                        return var.get('cachedSetTimeout').callprop('call', var.get(u"null"), var.get('fun'), Js(0.0))
                    except PyJsException as PyJsTempException:
                        PyJsHolder_65_63664642 = var.own.get('e')
                        var.force_own_put('e', PyExceptionToJs(PyJsTempException))
                        try:
                            return var.get('cachedSetTimeout').callprop('call', var.get(u"this"), var.get('fun'), Js(0.0))
                        finally:
                            if PyJsHolder_65_63664642 is not None:
                                var.own['e'] = PyJsHolder_65_63664642
                            else:
                                del var.own['e']
                            del PyJsHolder_65_63664642
                finally:
                    if PyJsHolder_65_44332318 is not None:
                        var.own['e'] = PyJsHolder_65_44332318
                    else:
                        del var.own['e']
                    del PyJsHolder_65_44332318
        PyJsHoisted_runTimeout_.func_name = 'runTimeout'
        var.put('runTimeout', PyJsHoisted_runTimeout_)
        @Js
        def PyJsHoisted_runClearTimeout_(marker, this, arguments, var=var):
            var = Scope({'marker':marker, 'this':this, 'arguments':arguments}, var)
            var.registers(['marker'])
            if PyJsStrictEq(var.get('cachedClearTimeout'),var.get('clearTimeout')):
                return var.get('clearTimeout')(var.get('marker'))
            if ((PyJsStrictEq(var.get('cachedClearTimeout'),var.get('defaultClearTimeout')) or var.get('cachedClearTimeout').neg()) and var.get('clearTimeout')):
                var.put('cachedClearTimeout', var.get('clearTimeout'))
                return var.get('clearTimeout')(var.get('marker'))
            try:
                return var.get('cachedClearTimeout')(var.get('marker'))
            except PyJsException as PyJsTempException:
                PyJsHolder_65_60343259 = var.own.get('e')
                var.force_own_put('e', PyExceptionToJs(PyJsTempException))
                try:
                    try:
                        return var.get('cachedClearTimeout').callprop('call', var.get(u"null"), var.get('marker'))
                    except PyJsException as PyJsTempException:
                        PyJsHolder_65_25912050 = var.own.get('e')
                        var.force_own_put('e', PyExceptionToJs(PyJsTempException))
                        try:
                            return var.get('cachedClearTimeout').callprop('call', var.get(u"this"), var.get('marker'))
                        finally:
                            if PyJsHolder_65_25912050 is not None:
                                var.own['e'] = PyJsHolder_65_25912050
                            else:
                                del var.own['e']
                            del PyJsHolder_65_25912050
                finally:
                    if PyJsHolder_65_60343259 is not None:
                        var.own['e'] = PyJsHolder_65_60343259
                    else:
                        del var.own['e']
                    del PyJsHolder_65_60343259
        PyJsHoisted_runClearTimeout_.func_name = 'runClearTimeout'
        var.put('runClearTimeout', PyJsHoisted_runClearTimeout_)
        @Js
        def PyJsHoisted_cleanUpNextTick_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            if (var.get('draining').neg() or var.get('currentQueue').neg()):
                return var.get('undefined')
            var.put('draining', Js(False))
            if var.get('currentQueue').get('length'):
                var.put('queue', var.get('currentQueue').callprop('concat', var.get('queue')))
            else:
                var.put('queueIndex', (-Js(1.0)))
            if var.get('queue').get('length'):
                var.get('drainQueue')()
        PyJsHoisted_cleanUpNextTick_.func_name = 'cleanUpNextTick'
        var.put('cleanUpNextTick', PyJsHoisted_cleanUpNextTick_)
        @Js
        def PyJsHoisted_drainQueue_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'timeout'])
            if var.get('draining'):
                return var.get('undefined')
            var.put('timeout', var.get('runTimeout')(var.get('cleanUpNextTick')))
            var.put('draining', Js(True))
            var.put('len', var.get('queue').get('length'))
            while var.get('len'):
                var.put('currentQueue', var.get('queue'))
                var.put('queue', Js([]))
                while (var.put('queueIndex',Js(var.get('queueIndex').to_number())+Js(1))<var.get('len')):
                    if var.get('currentQueue'):
                        var.get('currentQueue').get(var.get('queueIndex')).callprop('run')
                var.put('queueIndex', (-Js(1.0)))
                var.put('len', var.get('queue').get('length'))
            var.put('currentQueue', var.get(u"null"))
            var.put('draining', Js(False))
            var.get('runClearTimeout')(var.get('timeout'))
        PyJsHoisted_drainQueue_.func_name = 'drainQueue'
        var.put('drainQueue', PyJsHoisted_drainQueue_)
        @Js
        def PyJsHoisted_Item_(fun, array, this, arguments, var=var):
            var = Scope({'fun':fun, 'array':array, 'this':this, 'arguments':arguments}, var)
            var.registers(['fun', 'array'])
            var.get(u"this").put('fun', var.get('fun'))
            var.get(u"this").put('array', var.get('array'))
        PyJsHoisted_Item_.func_name = 'Item'
        var.put('Item', PyJsHoisted_Item_)
        @Js
        def PyJsHoisted_noop_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            pass
        PyJsHoisted_noop_.func_name = 'noop'
        var.put('noop', PyJsHoisted_noop_)
        var.put('process', var.get('module').put('exports', Js({})))
        pass
        pass
        pass
        pass
        @Js
        def PyJs_anonymous_75_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            try:
                if PyJsStrictEq(var.get('setTimeout',throw=False).typeof(),Js('function')):
                    var.put('cachedSetTimeout', var.get('setTimeout'))
                else:
                    var.put('cachedSetTimeout', var.get('defaultSetTimout'))
            except PyJsException as PyJsTempException:
                PyJsHolder_65_40702304 = var.own.get('e')
                var.force_own_put('e', PyExceptionToJs(PyJsTempException))
                try:
                    var.put('cachedSetTimeout', var.get('defaultSetTimout'))
                finally:
                    if PyJsHolder_65_40702304 is not None:
                        var.own['e'] = PyJsHolder_65_40702304
                    else:
                        del var.own['e']
                    del PyJsHolder_65_40702304
            try:
                if PyJsStrictEq(var.get('clearTimeout',throw=False).typeof(),Js('function')):
                    var.put('cachedClearTimeout', var.get('clearTimeout'))
                else:
                    var.put('cachedClearTimeout', var.get('defaultClearTimeout'))
            except PyJsException as PyJsTempException:
                PyJsHolder_65_63365950 = var.own.get('e')
                var.force_own_put('e', PyExceptionToJs(PyJsTempException))
                try:
                    var.put('cachedClearTimeout', var.get('defaultClearTimeout'))
                finally:
                    if PyJsHolder_65_63365950 is not None:
                        var.own['e'] = PyJsHolder_65_63365950
                    else:
                        del var.own['e']
                    del PyJsHolder_65_63365950
        PyJs_anonymous_75_._set_name('anonymous')
        PyJs_anonymous_75_()
        pass
        pass
        var.put('queue', Js([]))
        var.put('draining', Js(False))
        pass
        var.put('queueIndex', (-Js(1.0)))
        pass
        pass
        @Js
        def PyJs_anonymous_76_(fun, this, arguments, var=var):
            var = Scope({'fun':fun, 'this':this, 'arguments':arguments}, var)
            var.registers(['fun', 'args', 'i'])
            var.put('args', var.get('Array').create((var.get('arguments').get('length')-Js(1.0))))
            if (var.get('arguments').get('length')>Js(1.0)):
                #for JS loop
                var.put('i', Js(1.0))
                while (var.get('i')<var.get('arguments').get('length')):
                    try:
                        var.get('args').put((var.get('i')-Js(1.0)), var.get('arguments').get(var.get('i')))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.get('queue').callprop('push', var.get('Item').create(var.get('fun'), var.get('args')))
            if (PyJsStrictEq(var.get('queue').get('length'),Js(1.0)) and var.get('draining').neg()):
                var.get('runTimeout')(var.get('drainQueue'))
        PyJs_anonymous_76_._set_name('anonymous')
        var.get('process').put('nextTick', PyJs_anonymous_76_)
        pass
        @Js
        def PyJs_anonymous_77_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            var.get(u"this").get('fun').callprop('apply', var.get(u"null"), var.get(u"this").get('array'))
        PyJs_anonymous_77_._set_name('anonymous')
        var.get('Item').get('prototype').put('run', PyJs_anonymous_77_)
        var.get('process').put('title', Js('browser'))
        var.get('process').put('browser', Js(True))
        var.get('process').put('env', Js({}))
        var.get('process').put('argv', Js([]))
        var.get('process').put('version', Js(''))
        var.get('process').put('versions', Js({}))
        pass
        var.get('process').put('on', var.get('noop'))
        var.get('process').put('addListener', var.get('noop'))
        var.get('process').put('once', var.get('noop'))
        var.get('process').put('off', var.get('noop'))
        var.get('process').put('removeListener', var.get('noop'))
        var.get('process').put('removeAllListeners', var.get('noop'))
        var.get('process').put('emit', var.get('noop'))
        var.get('process').put('prependListener', var.get('noop'))
        var.get('process').put('prependOnceListener', var.get('noop'))
        @Js
        def PyJs_anonymous_78_(name, this, arguments, var=var):
            var = Scope({'name':name, 'this':this, 'arguments':arguments}, var)
            var.registers(['name'])
            return Js([])
        PyJs_anonymous_78_._set_name('anonymous')
        var.get('process').put('listeners', PyJs_anonymous_78_)
        @Js
        def PyJs_anonymous_79_(name, this, arguments, var=var):
            var = Scope({'name':name, 'this':this, 'arguments':arguments}, var)
            var.registers(['name'])
            PyJsTempException = JsToPyException(var.get('Error').create(Js('process.binding is not supported')))
            raise PyJsTempException
        PyJs_anonymous_79_._set_name('anonymous')
        var.get('process').put('binding', PyJs_anonymous_79_)
        @Js
        def PyJs_anonymous_80_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return Js('/')
        PyJs_anonymous_80_._set_name('anonymous')
        var.get('process').put('cwd', PyJs_anonymous_80_)
        @Js
        def PyJs_anonymous_81_(dir, this, arguments, var=var):
            var = Scope({'dir':dir, 'this':this, 'arguments':arguments}, var)
            var.registers(['dir'])
            PyJsTempException = JsToPyException(var.get('Error').create(Js('process.chdir is not supported')))
            raise PyJsTempException
        PyJs_anonymous_81_._set_name('anonymous')
        var.get('process').put('chdir', PyJs_anonymous_81_)
        @Js
        def PyJs_anonymous_82_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return Js(0.0)
        PyJs_anonymous_82_._set_name('anonymous')
        var.get('process').put('umask', PyJs_anonymous_82_)
    PyJs_anonymous_74_._set_name('anonymous')
    @Js
    def PyJs_anonymous_83_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['module', 'require', 'exports'])
        @Js
        def PyJs_anonymous_84_(setImmediate, clearImmediate, this, arguments, var=var):
            var = Scope({'setImmediate':setImmediate, 'clearImmediate':clearImmediate, 'this':this, 'arguments':arguments}, var)
            var.registers(['setImmediate', 'clearImmediate'])
            @Js
            def PyJs_anonymous_85_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers(['Timeout', 'immediateIds', 'nextImmediateId', 'apply', 'slice', 'nextTick'])
                @Js
                def PyJsHoisted_Timeout_(id, clearFn, this, arguments, var=var):
                    var = Scope({'id':id, 'clearFn':clearFn, 'this':this, 'arguments':arguments}, var)
                    var.registers(['id', 'clearFn'])
                    var.get(u"this").put('_id', var.get('id'))
                    var.get(u"this").put('_clearFn', var.get('clearFn'))
                PyJsHoisted_Timeout_.func_name = 'Timeout'
                var.put('Timeout', PyJsHoisted_Timeout_)
                var.put('nextTick', var.get('require')(Js('process/browser.js')).get('nextTick'))
                var.put('apply', var.get('Function').get('prototype').get('apply'))
                var.put('slice', var.get('Array').get('prototype').get('slice'))
                var.put('immediateIds', Js({}))
                var.put('nextImmediateId', Js(0.0))
                @Js
                def PyJs_anonymous_86_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    return var.get('Timeout').create(var.get('apply').callprop('call', var.get('setTimeout'), var.get('window'), var.get('arguments')), var.get('clearTimeout'))
                PyJs_anonymous_86_._set_name('anonymous')
                var.get('exports').put('setTimeout', PyJs_anonymous_86_)
                @Js
                def PyJs_anonymous_87_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    return var.get('Timeout').create(var.get('apply').callprop('call', var.get('setInterval'), var.get('window'), var.get('arguments')), var.get('clearInterval'))
                PyJs_anonymous_87_._set_name('anonymous')
                var.get('exports').put('setInterval', PyJs_anonymous_87_)
                @Js
                def PyJs_anonymous_88_(timeout, this, arguments, var=var):
                    var = Scope({'timeout':timeout, 'this':this, 'arguments':arguments}, var)
                    var.registers(['timeout'])
                    var.get('timeout').callprop('close')
                PyJs_anonymous_88_._set_name('anonymous')
                var.get('exports').put('clearTimeout', var.get('exports').put('clearInterval', PyJs_anonymous_88_))
                pass
                @Js
                def PyJs_anonymous_89_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    pass
                PyJs_anonymous_89_._set_name('anonymous')
                var.get('Timeout').get('prototype').put('unref', var.get('Timeout').get('prototype').put('ref', PyJs_anonymous_89_))
                @Js
                def PyJs_anonymous_90_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    var.get(u"this").get('_clearFn').callprop('call', var.get('window'), var.get(u"this").get('_id'))
                PyJs_anonymous_90_._set_name('anonymous')
                var.get('Timeout').get('prototype').put('close', PyJs_anonymous_90_)
                @Js
                def PyJs_anonymous_91_(item, msecs, this, arguments, var=var):
                    var = Scope({'item':item, 'msecs':msecs, 'this':this, 'arguments':arguments}, var)
                    var.registers(['msecs', 'item'])
                    var.get('clearTimeout')(var.get('item').get('_idleTimeoutId'))
                    var.get('item').put('_idleTimeout', var.get('msecs'))
                PyJs_anonymous_91_._set_name('anonymous')
                var.get('exports').put('enroll', PyJs_anonymous_91_)
                @Js
                def PyJs_anonymous_92_(item, this, arguments, var=var):
                    var = Scope({'item':item, 'this':this, 'arguments':arguments}, var)
                    var.registers(['item'])
                    var.get('clearTimeout')(var.get('item').get('_idleTimeoutId'))
                    var.get('item').put('_idleTimeout', (-Js(1.0)))
                PyJs_anonymous_92_._set_name('anonymous')
                var.get('exports').put('unenroll', PyJs_anonymous_92_)
                @Js
                def PyJs_anonymous_93_(item, this, arguments, var=var):
                    var = Scope({'item':item, 'this':this, 'arguments':arguments}, var)
                    var.registers(['item', 'msecs'])
                    var.get('clearTimeout')(var.get('item').get('_idleTimeoutId'))
                    var.put('msecs', var.get('item').get('_idleTimeout'))
                    if (var.get('msecs')>=Js(0.0)):
                        @Js
                        def PyJs_onTimeout_94_(this, arguments, var=var):
                            var = Scope({'this':this, 'arguments':arguments, 'onTimeout':PyJs_onTimeout_94_}, var)
                            var.registers([])
                            if var.get('item').get('_onTimeout'):
                                var.get('item').callprop('_onTimeout')
                        PyJs_onTimeout_94_._set_name('onTimeout')
                        var.get('item').put('_idleTimeoutId', var.get('setTimeout')(PyJs_onTimeout_94_, var.get('msecs')))
                PyJs_anonymous_93_._set_name('anonymous')
                var.get('exports').put('_unrefActive', var.get('exports').put('active', PyJs_anonymous_93_))
                @Js
                def PyJs_anonymous_95_(fn, this, arguments, var=var):
                    var = Scope({'fn':fn, 'this':this, 'arguments':arguments}, var)
                    var.registers(['args', 'id', 'fn'])
                    var.put('id', (var.put('nextImmediateId',Js(var.get('nextImmediateId').to_number())+Js(1))-Js(1)))
                    var.put('args', (Js(False) if (var.get('arguments').get('length')<Js(2.0)) else var.get('slice').callprop('call', var.get('arguments'), Js(1.0))))
                    var.get('immediateIds').put(var.get('id'), Js(True))
                    @Js
                    def PyJs_onNextTick_96_(this, arguments, var=var):
                        var = Scope({'this':this, 'arguments':arguments, 'onNextTick':PyJs_onNextTick_96_}, var)
                        var.registers([])
                        if var.get('immediateIds').get(var.get('id')):
                            if var.get('args'):
                                var.get('fn').callprop('apply', var.get(u"null"), var.get('args'))
                            else:
                                var.get('fn').callprop('call', var.get(u"null"))
                            var.get('exports').callprop('clearImmediate', var.get('id'))
                    PyJs_onNextTick_96_._set_name('onNextTick')
                    var.get('nextTick')(PyJs_onNextTick_96_)
                    return var.get('id')
                PyJs_anonymous_95_._set_name('anonymous')
                var.get('exports').put('setImmediate', (var.get('setImmediate') if PyJsStrictEq(var.get('setImmediate',throw=False).typeof(),Js('function')) else PyJs_anonymous_95_))
                @Js
                def PyJs_anonymous_97_(id, this, arguments, var=var):
                    var = Scope({'id':id, 'this':this, 'arguments':arguments}, var)
                    var.registers(['id'])
                    var.get('immediateIds').delete(var.get('id'))
                PyJs_anonymous_97_._set_name('anonymous')
                var.get('exports').put('clearImmediate', (var.get('clearImmediate') if PyJsStrictEq(var.get('clearImmediate',throw=False).typeof(),Js('function')) else PyJs_anonymous_97_))
            PyJs_anonymous_85_._set_name('anonymous')
            PyJs_anonymous_85_.callprop('call', var.get(u"this"))
        PyJs_anonymous_84_._set_name('anonymous')
        PyJs_anonymous_84_.callprop('call', var.get(u"this"), var.get('require')(Js('timers')).get('setImmediate'), var.get('require')(Js('timers')).get('clearImmediate'))
    PyJs_anonymous_83_._set_name('anonymous')
    @Js
    def PyJs_anonymous_98_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['quoteRegExp', 'getRequiredModules', 'require', 'exports', 'moduleNameReqExp', 'hasValuesInQueues', 'webpackBootstrapFunc', 'module', 'getModuleDependencies', 'isNumeric', 'dependencyRegExp'])
        @Js
        def PyJsHoisted_webpackBootstrapFunc_(modules, this, arguments, var=var):
            var = Scope({'modules':modules, 'this':this, 'arguments':arguments}, var)
            var.registers(['modules', 'installedModules', 'f', '__webpack_require__'])
            @Js
            def PyJsHoisted___webpack_require___(moduleId, this, arguments, var=var):
                var = Scope({'moduleId':moduleId, 'this':this, 'arguments':arguments}, var)
                var.registers(['module', 'moduleId'])
                if var.get('installedModules').get(var.get('moduleId')):
                    return var.get('installedModules').get(var.get('moduleId')).get('exports')
                var.put('module', var.get('installedModules').put(var.get('moduleId'), Js({'i':var.get('moduleId'),'l':Js(False),'exports':Js({})})))
                var.get('modules').get(var.get('moduleId')).callprop('call', var.get('module').get('exports'), var.get('module'), var.get('module').get('exports'), var.get('__webpack_require__'))
                var.get('module').put('l', Js(True))
                return var.get('module').get('exports')
            PyJsHoisted___webpack_require___.func_name = '__webpack_require__'
            var.put('__webpack_require__', PyJsHoisted___webpack_require___)
            var.put('installedModules', Js({}))
            pass
            var.get('__webpack_require__').put('m', var.get('modules'))
            var.get('__webpack_require__').put('c', var.get('installedModules'))
            @Js
            def PyJs_anonymous_99_(value, this, arguments, var=var):
                var = Scope({'value':value, 'this':this, 'arguments':arguments}, var)
                var.registers(['value'])
                return var.get('value')
            PyJs_anonymous_99_._set_name('anonymous')
            var.get('__webpack_require__').put('i', PyJs_anonymous_99_)
            @Js
            def PyJs_anonymous_100_(exports, name, getter, this, arguments, var=var):
                var = Scope({'exports':exports, 'name':name, 'getter':getter, 'this':this, 'arguments':arguments}, var)
                var.registers(['getter', 'name', 'exports'])
                if var.get('__webpack_require__').callprop('o', var.get('exports'), var.get('name')).neg():
                    var.get('Object').callprop('defineProperty', var.get('exports'), var.get('name'), Js({'configurable':Js(False),'enumerable':Js(True),'get':var.get('getter')}))
            PyJs_anonymous_100_._set_name('anonymous')
            var.get('__webpack_require__').put('d', PyJs_anonymous_100_)
            @Js
            def PyJs_anonymous_101_(exports, this, arguments, var=var):
                var = Scope({'exports':exports, 'this':this, 'arguments':arguments}, var)
                var.registers(['exports'])
                var.get('Object').callprop('defineProperty', var.get('exports'), Js('__esModule'), Js({'value':Js(True)}))
            PyJs_anonymous_101_._set_name('anonymous')
            var.get('__webpack_require__').put('r', PyJs_anonymous_101_)
            @Js
            def PyJs_anonymous_102_(module, this, arguments, var=var):
                var = Scope({'module':module, 'this':this, 'arguments':arguments}, var)
                var.registers(['getter', 'module'])
                @Js
                def PyJs_getDefault_103_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments, 'getDefault':PyJs_getDefault_103_}, var)
                    var.registers([])
                    return var.get('module').get('default')
                PyJs_getDefault_103_._set_name('getDefault')
                @Js
                def PyJs_getModuleExports_104_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments, 'getModuleExports':PyJs_getModuleExports_104_}, var)
                    var.registers([])
                    return var.get('module')
                PyJs_getModuleExports_104_._set_name('getModuleExports')
                var.put('getter', (PyJs_getDefault_103_ if (var.get('module') and var.get('module').get('__esModule')) else PyJs_getModuleExports_104_))
                var.get('__webpack_require__').callprop('d', var.get('getter'), Js('a'), var.get('getter'))
                return var.get('getter')
            PyJs_anonymous_102_._set_name('anonymous')
            var.get('__webpack_require__').put('n', PyJs_anonymous_102_)
            @Js
            def PyJs_anonymous_105_(object, property, this, arguments, var=var):
                var = Scope({'object':object, 'property':property, 'this':this, 'arguments':arguments}, var)
                var.registers(['object', 'property'])
                return var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get('object'), var.get('property'))
            PyJs_anonymous_105_._set_name('anonymous')
            var.get('__webpack_require__').put('o', PyJs_anonymous_105_)
            var.get('__webpack_require__').put('p', Js('/'))
            @Js
            def PyJs_anonymous_106_(err, this, arguments, var=var):
                var = Scope({'err':err, 'this':this, 'arguments':arguments}, var)
                var.registers(['err'])
                var.get('console').callprop('error', var.get('err'))
                PyJsTempException = JsToPyException(var.get('err'))
                raise PyJsTempException
            PyJs_anonymous_106_._set_name('anonymous')
            var.get('__webpack_require__').put('oe', PyJs_anonymous_106_)
            var.put('f', var.get('__webpack_require__')(var.get('__webpack_require__').put('s', var.get('ENTRY_MODULE'))))
            return (var.get('f').get('default') or var.get('f'))
        PyJsHoisted_webpackBootstrapFunc_.func_name = 'webpackBootstrapFunc'
        var.put('webpackBootstrapFunc', PyJsHoisted_webpackBootstrapFunc_)
        @Js
        def PyJsHoisted_quoteRegExp_(str, this, arguments, var=var):
            var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
            var.registers(['str'])
            return (var.get('str')+Js('')).callprop('replace', JsRegExp('/[.?*+^$[\\]\\\\(){}|-]/g'), Js('\\$&'))
        PyJsHoisted_quoteRegExp_.func_name = 'quoteRegExp'
        var.put('quoteRegExp', PyJsHoisted_quoteRegExp_)
        @Js
        def PyJsHoisted_isNumeric_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get('isNaN')((Js(1.0)*var.get('n'))).neg()
        PyJsHoisted_isNumeric_.func_name = 'isNumeric'
        var.put('isNumeric', PyJsHoisted_isNumeric_)
        @Js
        def PyJsHoisted_getModuleDependencies_(sources, module, queueName, this, arguments, var=var):
            var = Scope({'sources':sources, 'module':module, 'queueName':queueName, 'this':this, 'arguments':arguments}, var)
            var.registers(['j', 'sources', 'queueName', 'fnString', 're', 'webpackRequireName', 'module', 'retval', 'match', 'keys', 'i', 'wrapperSignature'])
            var.put('retval', Js({}))
            var.get('retval').put(var.get('queueName'), Js([]))
            var.put('fnString', var.get('module').callprop('toString'))
            var.put('wrapperSignature', var.get('fnString').callprop('match', JsRegExp('/^function\\s?\\w*\\(\\w+,\\s*\\w+,\\s*(\\w+)\\)/')))
            if var.get('wrapperSignature').neg():
                return var.get('retval')
            var.put('webpackRequireName', var.get('wrapperSignature').get('1'))
            var.put('re', var.get('RegExp').create(((Js('(\\\\n|\\W)')+var.get('quoteRegExp')(var.get('webpackRequireName')))+var.get('dependencyRegExp')), Js('g')))
            pass
            while var.put('match', var.get('re').callprop('exec', var.get('fnString'))):
                if PyJsStrictEq(var.get('match').get('3'),Js('dll-reference')):
                    continue
                var.get('retval').get(var.get('queueName')).callprop('push', var.get('match').get('3'))
            var.put('re', var.get('RegExp').create((((((Js('\\(')+var.get('quoteRegExp')(var.get('webpackRequireName')))+Js('\\("(dll-reference\\s('))+var.get('moduleNameReqExp'))+Js('))"\\)\\)'))+var.get('dependencyRegExp')), Js('g')))
            while var.put('match', var.get('re').callprop('exec', var.get('fnString'))):
                if var.get('sources').get(var.get('match').get('2')).neg():
                    var.get('retval').get(var.get('queueName')).callprop('push', var.get('match').get('1'))
                    var.get('sources').put(var.get('match').get('2'), var.get('__webpack_require__')(var.get('match').get('1')).get('m'))
                var.get('retval').put(var.get('match').get('2'), (var.get('retval').get(var.get('match').get('2')) or Js([])))
                var.get('retval').get(var.get('match').get('2')).callprop('push', var.get('match').get('4'))
            var.put('keys', var.get('Object').callprop('keys', var.get('retval')))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('keys').get('length')):
                try:
                    #for JS loop
                    var.put('j', Js(0.0))
                    while (var.get('j')<var.get('retval').get(var.get('keys').get(var.get('i'))).get('length')):
                        try:
                            if var.get('isNumeric')(var.get('retval').get(var.get('keys').get(var.get('i'))).get(var.get('j'))):
                                var.get('retval').get(var.get('keys').get(var.get('i'))).put(var.get('j'), (Js(1.0)*var.get('retval').get(var.get('keys').get(var.get('i'))).get(var.get('j'))))
                        finally:
                                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            return var.get('retval')
        PyJsHoisted_getModuleDependencies_.func_name = 'getModuleDependencies'
        var.put('getModuleDependencies', PyJsHoisted_getModuleDependencies_)
        @Js
        def PyJsHoisted_hasValuesInQueues_(queues, this, arguments, var=var):
            var = Scope({'queues':queues, 'this':this, 'arguments':arguments}, var)
            var.registers(['keys', 'queues'])
            var.put('keys', var.get('Object').callprop('keys', var.get('queues')))
            @Js
            def PyJs_anonymous_107_(hasValues, key, this, arguments, var=var):
                var = Scope({'hasValues':hasValues, 'key':key, 'this':this, 'arguments':arguments}, var)
                var.registers(['key', 'hasValues'])
                return (var.get('hasValues') or (var.get('queues').get(var.get('key')).get('length')>Js(0.0)))
            PyJs_anonymous_107_._set_name('anonymous')
            return var.get('keys').callprop('reduce', PyJs_anonymous_107_, Js(False))
        PyJsHoisted_hasValuesInQueues_.func_name = 'hasValuesInQueues'
        var.put('hasValuesInQueues', PyJsHoisted_hasValuesInQueues_)
        @Js
        def PyJsHoisted_getRequiredModules_(sources, moduleId, this, arguments, var=var):
            var = Scope({'sources':sources, 'moduleId':moduleId, 'this':this, 'arguments':arguments}, var)
            var.registers(['j', 'newModulesKeys', 'sources', 'queueName', 'requiredModules', 'newModules', 'modulesQueue', 'queue', 'seenModules', 'moduleToCheck', 'moduleId', 'queues', 'i'])
            var.put('modulesQueue', Js({'main':Js([var.get('moduleId')])}))
            var.put('requiredModules', Js({'main':Js([])}))
            var.put('seenModules', Js({'main':Js({})}))
            while var.get('hasValuesInQueues')(var.get('modulesQueue')):
                var.put('queues', var.get('Object').callprop('keys', var.get('modulesQueue')))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('queues').get('length')):
                    try:
                        var.put('queueName', var.get('queues').get(var.get('i')))
                        var.put('queue', var.get('modulesQueue').get(var.get('queueName')))
                        var.put('moduleToCheck', var.get('queue').callprop('pop'))
                        var.get('seenModules').put(var.get('queueName'), (var.get('seenModules').get(var.get('queueName')) or Js({})))
                        if (var.get('seenModules').get(var.get('queueName')).get(var.get('moduleToCheck')) or var.get('sources').get(var.get('queueName')).get(var.get('moduleToCheck')).neg()):
                            continue
                        var.get('seenModules').get(var.get('queueName')).put(var.get('moduleToCheck'), Js(True))
                        var.get('requiredModules').put(var.get('queueName'), (var.get('requiredModules').get(var.get('queueName')) or Js([])))
                        var.get('requiredModules').get(var.get('queueName')).callprop('push', var.get('moduleToCheck'))
                        var.put('newModules', var.get('getModuleDependencies')(var.get('sources'), var.get('sources').get(var.get('queueName')).get(var.get('moduleToCheck')), var.get('queueName')))
                        var.put('newModulesKeys', var.get('Object').callprop('keys', var.get('newModules')))
                        #for JS loop
                        var.put('j', Js(0.0))
                        while (var.get('j')<var.get('newModulesKeys').get('length')):
                            try:
                                var.get('modulesQueue').put(var.get('newModulesKeys').get(var.get('j')), (var.get('modulesQueue').get(var.get('newModulesKeys').get(var.get('j'))) or Js([])))
                                var.get('modulesQueue').put(var.get('newModulesKeys').get(var.get('j')), var.get('modulesQueue').get(var.get('newModulesKeys').get(var.get('j'))).callprop('concat', var.get('newModules').get(var.get('newModulesKeys').get(var.get('j')))))
                            finally:
                                    (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            return var.get('requiredModules')
        PyJsHoisted_getRequiredModules_.func_name = 'getRequiredModules'
        var.put('getRequiredModules', PyJsHoisted_getRequiredModules_)
        pass
        var.put('moduleNameReqExp', Js('[\\.|\\-|\\+|\\w|/|@]+'))
        var.put('dependencyRegExp', ((Js('\\(\\s*(/\\*.*?\\*/)?\\s*.*?(')+var.get('moduleNameReqExp'))+Js(').*?\\)')))
        pass
        pass
        pass
        pass
        pass
        @Js
        def PyJs_anonymous_108_(moduleId, options, this, arguments, var=var):
            var = Scope({'moduleId':moduleId, 'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['worker', 'sources', 'requiredModules', 'options', 'blob', 'URL', 'workerUrl', 'moduleId', 'src'])
            var.put('options', (var.get('options') or Js({})))
            var.put('sources', Js({'main':var.get('__webpack_modules__')}))
            var.put('requiredModules', (Js({'main':var.get('Object').callprop('keys', var.get('sources').get('main'))}) if var.get('options').get('all') else var.get('getRequiredModules')(var.get('sources'), var.get('moduleId'))))
            var.put('src', Js(''))
            @Js
            def PyJs_anonymous_109_(module, this, arguments, var=var):
                var = Scope({'module':module, 'this':this, 'arguments':arguments}, var)
                var.registers(['module', 'entryModule'])
                var.put('entryModule', Js(0.0))
                while var.get('requiredModules').get(var.get('module')).get(var.get('entryModule')):
                    (var.put('entryModule',Js(var.get('entryModule').to_number())+Js(1))-Js(1))
                var.get('requiredModules').get(var.get('module')).callprop('push', var.get('entryModule'))
                var.get('sources').get(var.get('module')).put(var.get('entryModule'), Js('(function(module, exports, __webpack_require__) { module.exports = __webpack_require__; })'))
                @Js
                def PyJs_anonymous_110_(id, this, arguments, var=var):
                    var = Scope({'id':id, 'this':this, 'arguments':arguments}, var)
                    var.registers(['id'])
                    return (((Js('')+var.get('JSON').callprop('stringify', var.get('id')))+Js(': '))+var.get('sources').get(var.get('module')).get(var.get('id')).callprop('toString'))
                PyJs_anonymous_110_._set_name('anonymous')
                var.put('src', (((((((var.get('src')+Js('var '))+var.get('module'))+Js(' = ('))+var.get('webpackBootstrapFunc').callprop('toString').callprop('replace', Js('ENTRY_MODULE'), var.get('JSON').callprop('stringify', var.get('entryModule'))))+Js(')({'))+var.get('requiredModules').get(var.get('module')).callprop('map', PyJs_anonymous_110_).callprop('join', Js(',')))+Js('});\n')))
            PyJs_anonymous_109_._set_name('anonymous')
            @Js
            def PyJs_anonymous_111_(m, this, arguments, var=var):
                var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
                var.registers(['m'])
                return PyJsStrictNeq(var.get('m'),Js('main'))
            PyJs_anonymous_111_._set_name('anonymous')
            var.get('Object').callprop('keys', var.get('requiredModules')).callprop('filter', PyJs_anonymous_111_).callprop('forEach', PyJs_anonymous_109_)
            @Js
            def PyJs_anonymous_112_(id, this, arguments, var=var):
                var = Scope({'id':id, 'this':this, 'arguments':arguments}, var)
                var.registers(['id'])
                return (((Js('')+var.get('JSON').callprop('stringify', var.get('id')))+Js(': '))+var.get('sources').get('main').get(var.get('id')).callprop('toString'))
            PyJs_anonymous_112_._set_name('anonymous')
            var.put('src', (((((var.get('src')+Js('new (('))+var.get('webpackBootstrapFunc').callprop('toString').callprop('replace', Js('ENTRY_MODULE'), var.get('JSON').callprop('stringify', var.get('moduleId'))))+Js(')({'))+var.get('requiredModules').get('main').callprop('map', PyJs_anonymous_112_).callprop('join', Js(',')))+Js('}))(self);')))
            var.put('blob', var.get('window').get('Blob').create(Js([var.get('src')]), Js({'type':Js('text/javascript')})))
            if var.get('options').get('bare'):
                return var.get('blob')
            var.put('URL', (((var.get('window').get('URL') or var.get('window').get('webkitURL')) or var.get('window').get('mozURL')) or var.get('window').get('msURL')))
            var.put('workerUrl', var.get('URL').callprop('createObjectURL', var.get('blob')))
            var.put('worker', var.get('window').get('Worker').create(var.get('workerUrl')))
            var.get('worker').put('objectURL', var.get('workerUrl'))
            return var.get('worker')
        PyJs_anonymous_108_._set_name('anonymous')
        var.get('module').put('exports', PyJs_anonymous_108_)
    PyJs_anonymous_98_._set_name('anonymous')
    @Js
    def PyJs_anonymous_113_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['bundleFn', 'sources', 'stringify', 'require', 'cache', 'module', 'exports'])
        var.put('bundleFn', var.get('arguments').get('3'))
        var.put('sources', var.get('arguments').get('4'))
        var.put('cache', var.get('arguments').get('5'))
        var.put('stringify', var.get('JSON').get('stringify'))
        @Js
        def PyJs_anonymous_114_(fn, options, this, arguments, var=var):
            var = Scope({'fn':fn, 'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['worker', 'fn', 'resolveSources', 'scache', 'l', 'URL', 'blob', 'options', 'wcache', 'skey', 'workerSources', 'exp', 'key', 'workerUrl', 'wkey', 'src', 'cacheKeys', 'i'])
            @Js
            def PyJsHoisted_resolveSources_(key, this, arguments, var=var):
                var = Scope({'key':key, 'this':this, 'arguments':arguments}, var)
                var.registers(['depKey', 'depPath', 'key'])
                var.get('workerSources').put(var.get('key'), Js(True))
                for PyJsTemp in var.get('sources').get(var.get('key')).get('1'):
                    var.put('depPath', PyJsTemp)
                    var.put('depKey', var.get('sources').get(var.get('key')).get('1').get(var.get('depPath')))
                    if var.get('workerSources').get(var.get('depKey')).neg():
                        var.get('resolveSources')(var.get('depKey'))
            PyJsHoisted_resolveSources_.func_name = 'resolveSources'
            var.put('resolveSources', PyJsHoisted_resolveSources_)
            pass
            var.put('cacheKeys', var.get('Object').callprop('keys', var.get('cache')))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('l', var.get('cacheKeys').get('length'))
            while (var.get('i')<var.get('l')):
                try:
                    var.put('key', var.get('cacheKeys').get(var.get('i')))
                    var.put('exp', var.get('cache').get(var.get('key')).get('exports'))
                    if (PyJsStrictEq(var.get('exp'),var.get('fn')) or (var.get('exp') and PyJsStrictEq(var.get('exp').get('default'),var.get('fn')))):
                        var.put('wkey', var.get('key'))
                        break
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            if var.get('wkey').neg():
                var.put('wkey', var.get('Math').callprop('floor', (var.get('Math').callprop('pow', Js(16.0), Js(8.0))*var.get('Math').callprop('random'))).callprop('toString', Js(16.0)))
                var.put('wcache', Js({}))
                #for JS loop
                var.put('i', Js(0.0))
                var.put('l', var.get('cacheKeys').get('length'))
                while (var.get('i')<var.get('l')):
                    try:
                        var.put('key', var.get('cacheKeys').get(var.get('i')))
                        var.get('wcache').put(var.get('key'), var.get('key'))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                var.get('sources').put(var.get('wkey'), Js([((Js('function(require,module,exports){')+var.get('fn'))+Js('(self); }')), var.get('wcache')]))
            var.put('skey', var.get('Math').callprop('floor', (var.get('Math').callprop('pow', Js(16.0), Js(8.0))*var.get('Math').callprop('random'))).callprop('toString', Js(16.0)))
            var.put('scache', Js({}))
            var.get('scache').put(var.get('wkey'), var.get('wkey'))
            var.get('sources').put(var.get('skey'), Js([(((((Js('function(require,module,exports){')+Js('var f = require('))+var.get('stringify')(var.get('wkey')))+Js(');'))+Js('(f.default ? f.default : f)(self);'))+Js('}')), var.get('scache')]))
            var.put('workerSources', Js({}))
            var.get('resolveSources')(var.get('skey'))
            pass
            @Js
            def PyJs_anonymous_115_(key, this, arguments, var=var):
                var = Scope({'key':key, 'this':this, 'arguments':arguments}, var)
                var.registers(['key'])
                return (((((var.get('stringify')(var.get('key'))+Js(':['))+var.get('sources').get(var.get('key')).get('0'))+Js(','))+var.get('stringify')(var.get('sources').get(var.get('key')).get('1')))+Js(']'))
            PyJs_anonymous_115_._set_name('anonymous')
            var.put('src', ((((((Js('(')+var.get('bundleFn'))+Js(')({'))+var.get('Object').callprop('keys', var.get('workerSources')).callprop('map', PyJs_anonymous_115_).callprop('join', Js(',')))+Js('},{},['))+var.get('stringify')(var.get('skey')))+Js('])')))
            var.put('URL', (((var.get('window').get('URL') or var.get('window').get('webkitURL')) or var.get('window').get('mozURL')) or var.get('window').get('msURL')))
            var.put('blob', var.get('Blob').create(Js([var.get('src')]), Js({'type':Js('text/javascript')})))
            if (var.get('options') and var.get('options').get('bare')):
                return var.get('blob')
            var.put('workerUrl', var.get('URL').callprop('createObjectURL', var.get('blob')))
            var.put('worker', var.get('Worker').create(var.get('workerUrl')))
            var.get('worker').put('objectURL', var.get('workerUrl'))
            return var.get('worker')
        PyJs_anonymous_114_._set_name('anonymous')
        var.get('module').put('exports', PyJs_anonymous_114_)
    PyJs_anonymous_113_._set_name('anonymous')
    @Js
    def PyJs_anonymous_116_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['require', 'module', 'assign', 'ROSLIB', 'exports'])
        var.put('ROSLIB', (var.get(u"this").get('ROSLIB') or Js({'REVISION':Js('1.3.0')})))
        var.put('assign', var.get('require')(Js('object-assign')))
        var.get('assign')(var.get('ROSLIB'), var.get('require')(Js('./core')))
        var.get('assign')(var.get('ROSLIB'), var.get('require')(Js('./actionlib')))
        var.get('assign')(var.get('ROSLIB'), var.get('require')(Js('./math')))
        var.get('assign')(var.get('ROSLIB'), var.get('require')(Js('./tf')))
        var.get('assign')(var.get('ROSLIB'), var.get('require')(Js('./urdf')))
        var.get('module').put('exports', var.get('ROSLIB'))
    PyJs_anonymous_116_._set_name('anonymous')
    @Js
    def PyJs_anonymous_117_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['module', 'require', 'exports'])
        @Js
        def PyJs_anonymous_118_(PyJsArg_676c6f62616c_, this, arguments, var=var):
            var = Scope({'global':PyJsArg_676c6f62616c_, 'this':this, 'arguments':arguments}, var)
            var.registers(['global'])
            @Js
            def PyJs_anonymous_119_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers([])
                var.get('global').put('ROSLIB', var.get('require')(Js('./RosLib')))
            PyJs_anonymous_119_._set_name('anonymous')
            PyJs_anonymous_119_.callprop('call', var.get(u"this"))
        PyJs_anonymous_118_._set_name('anonymous')
        PyJs_anonymous_118_.callprop('call', var.get(u"this"), (var.get('global') if PyJsStrictNeq(var.get('global',throw=False).typeof(),Js('undefined')) else (var.get('self') if PyJsStrictNeq(var.get('self',throw=False).typeof(),Js('undefined')) else (var.get('window') if PyJsStrictNeq(var.get('window',throw=False).typeof(),Js('undefined')) else Js({})))))
    PyJs_anonymous_117_._set_name('anonymous')
    @Js
    def PyJs_anonymous_120_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['EventEmitter2', 'Message', 'ActionClient', 'require', 'Topic', 'module', 'exports'])
        @Js
        def PyJsHoisted_ActionClient_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['that', 'options', 'receivedStatus'])
            var.put('that', var.get(u"this"))
            var.put('options', (var.get('options') or Js({})))
            var.get(u"this").put('ros', var.get('options').get('ros'))
            var.get(u"this").put('serverName', var.get('options').get('serverName'))
            var.get(u"this").put('actionName', var.get('options').get('actionName'))
            var.get(u"this").put('timeout', var.get('options').get('timeout'))
            var.get(u"this").put('omitFeedback', var.get('options').get('omitFeedback'))
            var.get(u"this").put('omitStatus', var.get('options').get('omitStatus'))
            var.get(u"this").put('omitResult', var.get('options').get('omitResult'))
            var.get(u"this").put('goals', Js({}))
            var.put('receivedStatus', Js(False))
            var.get(u"this").put('feedbackListener', var.get('Topic').create(Js({'ros':var.get(u"this").get('ros'),'name':(var.get(u"this").get('serverName')+Js('/feedback')),'messageType':(var.get(u"this").get('actionName')+Js('Feedback'))})))
            var.get(u"this").put('statusListener', var.get('Topic').create(Js({'ros':var.get(u"this").get('ros'),'name':(var.get(u"this").get('serverName')+Js('/status')),'messageType':Js('actionlib_msgs/GoalStatusArray')})))
            var.get(u"this").put('resultListener', var.get('Topic').create(Js({'ros':var.get(u"this").get('ros'),'name':(var.get(u"this").get('serverName')+Js('/result')),'messageType':(var.get(u"this").get('actionName')+Js('Result'))})))
            var.get(u"this").put('goalTopic', var.get('Topic').create(Js({'ros':var.get(u"this").get('ros'),'name':(var.get(u"this").get('serverName')+Js('/goal')),'messageType':(var.get(u"this").get('actionName')+Js('Goal'))})))
            var.get(u"this").put('cancelTopic', var.get('Topic').create(Js({'ros':var.get(u"this").get('ros'),'name':(var.get(u"this").get('serverName')+Js('/cancel')),'messageType':Js('actionlib_msgs/GoalID')})))
            var.get(u"this").get('goalTopic').callprop('advertise')
            var.get(u"this").get('cancelTopic').callprop('advertise')
            if var.get(u"this").get('omitStatus').neg():
                @Js
                def PyJs_anonymous_121_(statusMessage, this, arguments, var=var):
                    var = Scope({'statusMessage':statusMessage, 'this':this, 'arguments':arguments}, var)
                    var.registers(['statusMessage'])
                    var.put('receivedStatus', Js(True))
                    @Js
                    def PyJs_anonymous_122_(status, this, arguments, var=var):
                        var = Scope({'status':status, 'this':this, 'arguments':arguments}, var)
                        var.registers(['goal', 'status'])
                        var.put('goal', var.get('that').get('goals').get(var.get('status').get('goal_id').get('id')))
                        if var.get('goal'):
                            var.get('goal').callprop('emit', Js('status'), var.get('status'))
                    PyJs_anonymous_122_._set_name('anonymous')
                    var.get('statusMessage').get('status_list').callprop('forEach', PyJs_anonymous_122_)
                PyJs_anonymous_121_._set_name('anonymous')
                var.get(u"this").get('statusListener').callprop('subscribe', PyJs_anonymous_121_)
            if var.get(u"this").get('omitFeedback').neg():
                @Js
                def PyJs_anonymous_123_(feedbackMessage, this, arguments, var=var):
                    var = Scope({'feedbackMessage':feedbackMessage, 'this':this, 'arguments':arguments}, var)
                    var.registers(['goal', 'feedbackMessage'])
                    var.put('goal', var.get('that').get('goals').get(var.get('feedbackMessage').get('status').get('goal_id').get('id')))
                    if var.get('goal'):
                        var.get('goal').callprop('emit', Js('status'), var.get('feedbackMessage').get('status'))
                        var.get('goal').callprop('emit', Js('feedback'), var.get('feedbackMessage').get('feedback'))
                PyJs_anonymous_123_._set_name('anonymous')
                var.get(u"this").get('feedbackListener').callprop('subscribe', PyJs_anonymous_123_)
            if var.get(u"this").get('omitResult').neg():
                @Js
                def PyJs_anonymous_124_(resultMessage, this, arguments, var=var):
                    var = Scope({'resultMessage':resultMessage, 'this':this, 'arguments':arguments}, var)
                    var.registers(['goal', 'resultMessage'])
                    var.put('goal', var.get('that').get('goals').get(var.get('resultMessage').get('status').get('goal_id').get('id')))
                    if var.get('goal'):
                        var.get('goal').callprop('emit', Js('status'), var.get('resultMessage').get('status'))
                        var.get('goal').callprop('emit', Js('result'), var.get('resultMessage').get('result'))
                PyJs_anonymous_124_._set_name('anonymous')
                var.get(u"this").get('resultListener').callprop('subscribe', PyJs_anonymous_124_)
            if var.get(u"this").get('timeout'):
                @Js
                def PyJs_anonymous_125_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    if var.get('receivedStatus').neg():
                        var.get('that').callprop('emit', Js('timeout'))
                PyJs_anonymous_125_._set_name('anonymous')
                var.get('setTimeout')(PyJs_anonymous_125_, var.get(u"this").get('timeout'))
        PyJsHoisted_ActionClient_.func_name = 'ActionClient'
        var.put('ActionClient', PyJsHoisted_ActionClient_)
        var.put('Topic', var.get('require')(Js('../core/Topic')))
        var.put('Message', var.get('require')(Js('../core/Message')))
        var.put('EventEmitter2', var.get('require')(Js('eventemitter2')).get('EventEmitter2'))
        pass
        var.get('ActionClient').get('prototype').put('__proto__', var.get('EventEmitter2').get('prototype'))
        @Js
        def PyJs_anonymous_126_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['cancelMessage'])
            var.put('cancelMessage', var.get('Message').create())
            var.get(u"this").get('cancelTopic').callprop('publish', var.get('cancelMessage'))
        PyJs_anonymous_126_._set_name('anonymous')
        var.get('ActionClient').get('prototype').put('cancel', PyJs_anonymous_126_)
        @Js
        def PyJs_anonymous_127_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            var.get(u"this").get('goalTopic').callprop('unadvertise')
            var.get(u"this").get('cancelTopic').callprop('unadvertise')
            if var.get(u"this").get('omitStatus').neg():
                var.get(u"this").get('statusListener').callprop('unsubscribe')
            if var.get(u"this").get('omitFeedback').neg():
                var.get(u"this").get('feedbackListener').callprop('unsubscribe')
            if var.get(u"this").get('omitResult').neg():
                var.get(u"this").get('resultListener').callprop('unsubscribe')
        PyJs_anonymous_127_._set_name('anonymous')
        var.get('ActionClient').get('prototype').put('dispose', PyJs_anonymous_127_)
        var.get('module').put('exports', var.get('ActionClient'))
    PyJs_anonymous_120_._set_name('anonymous')
    @Js
    def PyJs_anonymous_128_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['EventEmitter2', 'Message', 'require', 'Topic', 'module', 'ActionListener', 'exports'])
        @Js
        def PyJsHoisted_ActionListener_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['resultListener', 'options', 'feedbackListener', 'that', 'goalListener', 'statusListener'])
            var.put('that', var.get(u"this"))
            var.put('options', (var.get('options') or Js({})))
            var.get(u"this").put('ros', var.get('options').get('ros'))
            var.get(u"this").put('serverName', var.get('options').get('serverName'))
            var.get(u"this").put('actionName', var.get('options').get('actionName'))
            var.get(u"this").put('timeout', var.get('options').get('timeout'))
            var.get(u"this").put('omitFeedback', var.get('options').get('omitFeedback'))
            var.get(u"this").put('omitStatus', var.get('options').get('omitStatus'))
            var.get(u"this").put('omitResult', var.get('options').get('omitResult'))
            var.put('goalListener', var.get('Topic').create(Js({'ros':var.get(u"this").get('ros'),'name':(var.get(u"this").get('serverName')+Js('/goal')),'messageType':(var.get(u"this").get('actionName')+Js('Goal'))})))
            var.put('feedbackListener', var.get('Topic').create(Js({'ros':var.get(u"this").get('ros'),'name':(var.get(u"this").get('serverName')+Js('/feedback')),'messageType':(var.get(u"this").get('actionName')+Js('Feedback'))})))
            var.put('statusListener', var.get('Topic').create(Js({'ros':var.get(u"this").get('ros'),'name':(var.get(u"this").get('serverName')+Js('/status')),'messageType':Js('actionlib_msgs/GoalStatusArray')})))
            var.put('resultListener', var.get('Topic').create(Js({'ros':var.get(u"this").get('ros'),'name':(var.get(u"this").get('serverName')+Js('/result')),'messageType':(var.get(u"this").get('actionName')+Js('Result'))})))
            @Js
            def PyJs_anonymous_129_(goalMessage, this, arguments, var=var):
                var = Scope({'goalMessage':goalMessage, 'this':this, 'arguments':arguments}, var)
                var.registers(['goalMessage'])
                var.get('that').callprop('emit', Js('goal'), var.get('goalMessage'))
            PyJs_anonymous_129_._set_name('anonymous')
            var.get('goalListener').callprop('subscribe', PyJs_anonymous_129_)
            @Js
            def PyJs_anonymous_130_(statusMessage, this, arguments, var=var):
                var = Scope({'statusMessage':statusMessage, 'this':this, 'arguments':arguments}, var)
                var.registers(['statusMessage'])
                @Js
                def PyJs_anonymous_131_(status, this, arguments, var=var):
                    var = Scope({'status':status, 'this':this, 'arguments':arguments}, var)
                    var.registers(['status'])
                    var.get('that').callprop('emit', Js('status'), var.get('status'))
                PyJs_anonymous_131_._set_name('anonymous')
                var.get('statusMessage').get('status_list').callprop('forEach', PyJs_anonymous_131_)
            PyJs_anonymous_130_._set_name('anonymous')
            var.get('statusListener').callprop('subscribe', PyJs_anonymous_130_)
            @Js
            def PyJs_anonymous_132_(feedbackMessage, this, arguments, var=var):
                var = Scope({'feedbackMessage':feedbackMessage, 'this':this, 'arguments':arguments}, var)
                var.registers(['feedbackMessage'])
                var.get('that').callprop('emit', Js('status'), var.get('feedbackMessage').get('status'))
                var.get('that').callprop('emit', Js('feedback'), var.get('feedbackMessage').get('feedback'))
            PyJs_anonymous_132_._set_name('anonymous')
            var.get('feedbackListener').callprop('subscribe', PyJs_anonymous_132_)
            @Js
            def PyJs_anonymous_133_(resultMessage, this, arguments, var=var):
                var = Scope({'resultMessage':resultMessage, 'this':this, 'arguments':arguments}, var)
                var.registers(['resultMessage'])
                var.get('that').callprop('emit', Js('status'), var.get('resultMessage').get('status'))
                var.get('that').callprop('emit', Js('result'), var.get('resultMessage').get('result'))
            PyJs_anonymous_133_._set_name('anonymous')
            var.get('resultListener').callprop('subscribe', PyJs_anonymous_133_)
        PyJsHoisted_ActionListener_.func_name = 'ActionListener'
        var.put('ActionListener', PyJsHoisted_ActionListener_)
        var.put('Topic', var.get('require')(Js('../core/Topic')))
        var.put('Message', var.get('require')(Js('../core/Message')))
        var.put('EventEmitter2', var.get('require')(Js('eventemitter2')).get('EventEmitter2'))
        pass
        var.get('ActionListener').get('prototype').put('__proto__', var.get('EventEmitter2').get('prototype'))
        var.get('module').put('exports', var.get('ActionListener'))
    PyJs_anonymous_128_._set_name('anonymous')
    @Js
    def PyJs_anonymous_134_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['EventEmitter2', 'Message', 'require', 'module', 'Goal', 'exports'])
        @Js
        def PyJsHoisted_Goal_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['that', 'date', 'options'])
            var.put('that', var.get(u"this"))
            var.get(u"this").put('actionClient', var.get('options').get('actionClient'))
            var.get(u"this").put('goalMessage', var.get('options').get('goalMessage'))
            var.get(u"this").put('isFinished', Js(False))
            var.put('date', var.get('Date').create())
            var.get(u"this").put('goalID', (((Js('goal_')+var.get('Math').callprop('random'))+Js('_'))+var.get('date').callprop('getTime')))
            var.get(u"this").put('goalMessage', var.get('Message').create(Js({'goal_id':Js({'stamp':Js({'secs':Js(0.0),'nsecs':Js(0.0)}),'id':var.get(u"this").get('goalID')}),'goal':var.get(u"this").get('goalMessage')})))
            @Js
            def PyJs_anonymous_135_(status, this, arguments, var=var):
                var = Scope({'status':status, 'this':this, 'arguments':arguments}, var)
                var.registers(['status'])
                var.get('that').put('status', var.get('status'))
            PyJs_anonymous_135_._set_name('anonymous')
            var.get(u"this").callprop('on', Js('status'), PyJs_anonymous_135_)
            @Js
            def PyJs_anonymous_136_(result, this, arguments, var=var):
                var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                var.registers(['result'])
                var.get('that').put('isFinished', Js(True))
                var.get('that').put('result', var.get('result'))
            PyJs_anonymous_136_._set_name('anonymous')
            var.get(u"this").callprop('on', Js('result'), PyJs_anonymous_136_)
            @Js
            def PyJs_anonymous_137_(feedback, this, arguments, var=var):
                var = Scope({'feedback':feedback, 'this':this, 'arguments':arguments}, var)
                var.registers(['feedback'])
                var.get('that').put('feedback', var.get('feedback'))
            PyJs_anonymous_137_._set_name('anonymous')
            var.get(u"this").callprop('on', Js('feedback'), PyJs_anonymous_137_)
            var.get(u"this").get('actionClient').get('goals').put(var.get(u"this").get('goalID'), var.get(u"this"))
        PyJsHoisted_Goal_.func_name = 'Goal'
        var.put('Goal', PyJsHoisted_Goal_)
        var.put('Message', var.get('require')(Js('../core/Message')))
        var.put('EventEmitter2', var.get('require')(Js('eventemitter2')).get('EventEmitter2'))
        pass
        var.get('Goal').get('prototype').put('__proto__', var.get('EventEmitter2').get('prototype'))
        @Js
        def PyJs_anonymous_138_(timeout, this, arguments, var=var):
            var = Scope({'timeout':timeout, 'this':this, 'arguments':arguments}, var)
            var.registers(['that', 'timeout'])
            var.put('that', var.get(u"this"))
            var.get('that').get('actionClient').get('goalTopic').callprop('publish', var.get('that').get('goalMessage'))
            if var.get('timeout'):
                @Js
                def PyJs_anonymous_139_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    if var.get('that').get('isFinished').neg():
                        var.get('that').callprop('emit', Js('timeout'))
                PyJs_anonymous_139_._set_name('anonymous')
                var.get('setTimeout')(PyJs_anonymous_139_, var.get('timeout'))
        PyJs_anonymous_138_._set_name('anonymous')
        var.get('Goal').get('prototype').put('send', PyJs_anonymous_138_)
        @Js
        def PyJs_anonymous_140_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['cancelMessage'])
            var.put('cancelMessage', var.get('Message').create(Js({'id':var.get(u"this").get('goalID')})))
            var.get(u"this").get('actionClient').get('cancelTopic').callprop('publish', var.get('cancelMessage'))
        PyJs_anonymous_140_._set_name('anonymous')
        var.get('Goal').get('prototype').put('cancel', PyJs_anonymous_140_)
        var.get('module').put('exports', var.get('Goal'))
    PyJs_anonymous_134_._set_name('anonymous')
    @Js
    def PyJs_anonymous_141_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['EventEmitter2', 'Message', 'SimpleActionServer', 'require', 'Topic', 'module', 'exports'])
        @Js
        def PyJsHoisted_SimpleActionServer_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['statusPublisher', 'goalListener', 'cancelListener', 'options', 'isEarlier', 'statusInterval', 'that'])
            var.put('that', var.get(u"this"))
            var.put('options', (var.get('options') or Js({})))
            var.get(u"this").put('ros', var.get('options').get('ros'))
            var.get(u"this").put('serverName', var.get('options').get('serverName'))
            var.get(u"this").put('actionName', var.get('options').get('actionName'))
            var.get(u"this").put('feedbackPublisher', var.get('Topic').create(Js({'ros':var.get(u"this").get('ros'),'name':(var.get(u"this").get('serverName')+Js('/feedback')),'messageType':(var.get(u"this").get('actionName')+Js('Feedback'))})))
            var.get(u"this").get('feedbackPublisher').callprop('advertise')
            var.put('statusPublisher', var.get('Topic').create(Js({'ros':var.get(u"this").get('ros'),'name':(var.get(u"this").get('serverName')+Js('/status')),'messageType':Js('actionlib_msgs/GoalStatusArray')})))
            var.get('statusPublisher').callprop('advertise')
            var.get(u"this").put('resultPublisher', var.get('Topic').create(Js({'ros':var.get(u"this").get('ros'),'name':(var.get(u"this").get('serverName')+Js('/result')),'messageType':(var.get(u"this").get('actionName')+Js('Result'))})))
            var.get(u"this").get('resultPublisher').callprop('advertise')
            var.put('goalListener', var.get('Topic').create(Js({'ros':var.get(u"this").get('ros'),'name':(var.get(u"this").get('serverName')+Js('/goal')),'messageType':(var.get(u"this").get('actionName')+Js('Goal'))})))
            var.put('cancelListener', var.get('Topic').create(Js({'ros':var.get(u"this").get('ros'),'name':(var.get(u"this").get('serverName')+Js('/cancel')),'messageType':Js('actionlib_msgs/GoalID')})))
            var.get(u"this").put('statusMessage', var.get('Message').create(Js({'header':Js({'stamp':Js({'secs':Js(0.0),'nsecs':Js(100.0)}),'frame_id':Js('')}),'status_list':Js([])})))
            var.get(u"this").put('currentGoal', var.get(u"null"))
            var.get(u"this").put('nextGoal', var.get(u"null"))
            @Js
            def PyJs_anonymous_142_(goalMessage, this, arguments, var=var):
                var = Scope({'goalMessage':goalMessage, 'this':this, 'arguments':arguments}, var)
                var.registers(['goalMessage'])
                if var.get('that').get('currentGoal'):
                    var.get('that').put('nextGoal', var.get('goalMessage'))
                    var.get('that').callprop('emit', Js('cancel'))
                else:
                    var.get('that').get('statusMessage').put('status_list', Js([Js({'goal_id':var.get('goalMessage').get('goal_id'),'status':Js(1.0)})]))
                    var.get('that').put('currentGoal', var.get('goalMessage'))
                    var.get('that').callprop('emit', Js('goal'), var.get('goalMessage').get('goal'))
            PyJs_anonymous_142_._set_name('anonymous')
            var.get('goalListener').callprop('subscribe', PyJs_anonymous_142_)
            @Js
            def PyJs_anonymous_143_(t1, t2, this, arguments, var=var):
                var = Scope({'t1':t1, 't2':t2, 'this':this, 'arguments':arguments}, var)
                var.registers(['t1', 't2'])
                if (var.get('t1').get('secs')>var.get('t2').get('secs')):
                    return Js(False)
                else:
                    if (var.get('t1').get('secs')<var.get('t2').get('secs')):
                        return Js(True)
                    else:
                        if (var.get('t1').get('nsecs')<var.get('t2').get('nsecs')):
                            return Js(True)
                        else:
                            return Js(False)
            PyJs_anonymous_143_._set_name('anonymous')
            var.put('isEarlier', PyJs_anonymous_143_)
            @Js
            def PyJs_anonymous_144_(cancelMessage, this, arguments, var=var):
                var = Scope({'cancelMessage':cancelMessage, 'this':this, 'arguments':arguments}, var)
                var.registers(['cancelMessage'])
                if ((PyJsStrictEq(var.get('cancelMessage').get('stamp').get('secs'),Js(0.0)) and PyJsStrictEq(var.get('cancelMessage').get('stamp').get('secs'),Js(0.0))) and PyJsStrictEq(var.get('cancelMessage').get('id'),Js(''))):
                    var.get('that').put('nextGoal', var.get(u"null"))
                    if var.get('that').get('currentGoal'):
                        var.get('that').callprop('emit', Js('cancel'))
                else:
                    if (var.get('that').get('currentGoal') and PyJsStrictEq(var.get('cancelMessage').get('id'),var.get('that').get('currentGoal').get('goal_id').get('id'))):
                        var.get('that').callprop('emit', Js('cancel'))
                    else:
                        if (var.get('that').get('nextGoal') and PyJsStrictEq(var.get('cancelMessage').get('id'),var.get('that').get('nextGoal').get('goal_id').get('id'))):
                            var.get('that').put('nextGoal', var.get(u"null"))
                    if (var.get('that').get('nextGoal') and var.get('isEarlier')(var.get('that').get('nextGoal').get('goal_id').get('stamp'), var.get('cancelMessage').get('stamp'))):
                        var.get('that').put('nextGoal', var.get(u"null"))
                    if (var.get('that').get('currentGoal') and var.get('isEarlier')(var.get('that').get('currentGoal').get('goal_id').get('stamp'), var.get('cancelMessage').get('stamp'))):
                        var.get('that').callprop('emit', Js('cancel'))
            PyJs_anonymous_144_._set_name('anonymous')
            var.get('cancelListener').callprop('subscribe', PyJs_anonymous_144_)
            @Js
            def PyJs_anonymous_145_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers(['nsecs', 'secs', 'currentTime'])
                var.put('currentTime', var.get('Date').create())
                var.put('secs', var.get('Math').callprop('floor', (var.get('currentTime').callprop('getTime')/Js(1000.0))))
                var.put('nsecs', var.get('Math').callprop('round', (Js(1000000000.0)*((var.get('currentTime').callprop('getTime')/Js(1000.0))-var.get('secs')))))
                var.get('that').get('statusMessage').get('header').get('stamp').put('secs', var.get('secs'))
                var.get('that').get('statusMessage').get('header').get('stamp').put('nsecs', var.get('nsecs'))
                var.get('statusPublisher').callprop('publish', var.get('that').get('statusMessage'))
            PyJs_anonymous_145_._set_name('anonymous')
            var.put('statusInterval', var.get('setInterval')(PyJs_anonymous_145_, Js(500.0)))
        PyJsHoisted_SimpleActionServer_.func_name = 'SimpleActionServer'
        var.put('SimpleActionServer', PyJsHoisted_SimpleActionServer_)
        var.put('Topic', var.get('require')(Js('../core/Topic')))
        var.put('Message', var.get('require')(Js('../core/Message')))
        var.put('EventEmitter2', var.get('require')(Js('eventemitter2')).get('EventEmitter2'))
        pass
        var.get('SimpleActionServer').get('prototype').put('__proto__', var.get('EventEmitter2').get('prototype'))
        @Js
        def PyJs_anonymous_146_(result2, this, arguments, var=var):
            var = Scope({'result2':result2, 'this':this, 'arguments':arguments}, var)
            var.registers(['result2', 'resultMessage'])
            var.put('resultMessage', var.get('Message').create(Js({'status':Js({'goal_id':var.get(u"this").get('currentGoal').get('goal_id'),'status':Js(3.0)}),'result':var.get('result2')})))
            var.get(u"this").get('resultPublisher').callprop('publish', var.get('resultMessage'))
            var.get(u"this").get('statusMessage').put('status_list', Js([]))
            if var.get(u"this").get('nextGoal'):
                var.get(u"this").put('currentGoal', var.get(u"this").get('nextGoal'))
                var.get(u"this").put('nextGoal', var.get(u"null"))
                var.get(u"this").callprop('emit', Js('goal'), var.get(u"this").get('currentGoal').get('goal'))
            else:
                var.get(u"this").put('currentGoal', var.get(u"null"))
        PyJs_anonymous_146_._set_name('anonymous')
        var.get('SimpleActionServer').get('prototype').put('setSucceeded', PyJs_anonymous_146_)
        @Js
        def PyJs_anonymous_147_(result2, this, arguments, var=var):
            var = Scope({'result2':result2, 'this':this, 'arguments':arguments}, var)
            var.registers(['result2', 'resultMessage'])
            var.put('resultMessage', var.get('Message').create(Js({'status':Js({'goal_id':var.get(u"this").get('currentGoal').get('goal_id'),'status':Js(4.0)}),'result':var.get('result2')})))
            var.get(u"this").get('resultPublisher').callprop('publish', var.get('resultMessage'))
            var.get(u"this").get('statusMessage').put('status_list', Js([]))
            if var.get(u"this").get('nextGoal'):
                var.get(u"this").put('currentGoal', var.get(u"this").get('nextGoal'))
                var.get(u"this").put('nextGoal', var.get(u"null"))
                var.get(u"this").callprop('emit', Js('goal'), var.get(u"this").get('currentGoal').get('goal'))
            else:
                var.get(u"this").put('currentGoal', var.get(u"null"))
        PyJs_anonymous_147_._set_name('anonymous')
        var.get('SimpleActionServer').get('prototype').put('setAborted', PyJs_anonymous_147_)
        @Js
        def PyJs_anonymous_148_(feedback2, this, arguments, var=var):
            var = Scope({'feedback2':feedback2, 'this':this, 'arguments':arguments}, var)
            var.registers(['feedback2', 'feedbackMessage'])
            var.put('feedbackMessage', var.get('Message').create(Js({'status':Js({'goal_id':var.get(u"this").get('currentGoal').get('goal_id'),'status':Js(1.0)}),'feedback':var.get('feedback2')})))
            var.get(u"this").get('feedbackPublisher').callprop('publish', var.get('feedbackMessage'))
        PyJs_anonymous_148_._set_name('anonymous')
        var.get('SimpleActionServer').get('prototype').put('sendFeedback', PyJs_anonymous_148_)
        @Js
        def PyJs_anonymous_149_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['resultMessage'])
            var.get(u"this").get('statusMessage').put('status_list', Js([]))
            var.put('resultMessage', var.get('Message').create(Js({'status':Js({'goal_id':var.get(u"this").get('currentGoal').get('goal_id'),'status':Js(2.0)})})))
            var.get(u"this").get('resultPublisher').callprop('publish', var.get('resultMessage'))
            if var.get(u"this").get('nextGoal'):
                var.get(u"this").put('currentGoal', var.get(u"this").get('nextGoal'))
                var.get(u"this").put('nextGoal', var.get(u"null"))
                var.get(u"this").callprop('emit', Js('goal'), var.get(u"this").get('currentGoal').get('goal'))
            else:
                var.get(u"this").put('currentGoal', var.get(u"null"))
        PyJs_anonymous_149_._set_name('anonymous')
        var.get('SimpleActionServer').get('prototype').put('setPreempted', PyJs_anonymous_149_)
        var.get('module').put('exports', var.get('SimpleActionServer'))
    PyJs_anonymous_141_._set_name('anonymous')
    @Js
    def PyJs_anonymous_150_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['mixin', 'require', 'Ros', 'module', 'action', 'exports'])
        var.put('Ros', var.get('require')(Js('../core/Ros')))
        var.put('mixin', var.get('require')(Js('../mixin')))
        var.put('action', var.get('module').put('exports', Js({'ActionClient':var.get('require')(Js('./ActionClient')),'ActionListener':var.get('require')(Js('./ActionListener')),'Goal':var.get('require')(Js('./Goal')),'SimpleActionServer':var.get('require')(Js('./SimpleActionServer'))})))
        var.get('mixin')(var.get('Ros'), Js([Js('ActionClient'), Js('SimpleActionServer')]), var.get('action'))
    PyJs_anonymous_150_._set_name('anonymous')
    @Js
    def PyJs_anonymous_151_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['Message', 'require', 'module', 'assign', 'exports'])
        @Js
        def PyJsHoisted_Message_(values, this, arguments, var=var):
            var = Scope({'values':values, 'this':this, 'arguments':arguments}, var)
            var.registers(['values'])
            var.get('assign')(var.get(u"this"), var.get('values'))
        PyJsHoisted_Message_.func_name = 'Message'
        var.put('Message', PyJsHoisted_Message_)
        var.put('assign', var.get('require')(Js('object-assign')))
        pass
        var.get('module').put('exports', var.get('Message'))
    PyJs_anonymous_151_._set_name('anonymous')
    @Js
    def PyJs_anonymous_152_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['require', 'module', 'Param', 'Service', 'ServiceRequest', 'exports'])
        @Js
        def PyJsHoisted_Param_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['options'])
            var.put('options', (var.get('options') or Js({})))
            var.get(u"this").put('ros', var.get('options').get('ros'))
            var.get(u"this").put('name', var.get('options').get('name'))
        PyJsHoisted_Param_.func_name = 'Param'
        var.put('Param', PyJsHoisted_Param_)
        var.put('Service', var.get('require')(Js('./Service')))
        var.put('ServiceRequest', var.get('require')(Js('./ServiceRequest')))
        pass
        @Js
        def PyJs_anonymous_153_(callback, this, arguments, var=var):
            var = Scope({'callback':callback, 'this':this, 'arguments':arguments}, var)
            var.registers(['callback', 'request', 'paramClient'])
            var.put('paramClient', var.get('Service').create(Js({'ros':var.get(u"this").get('ros'),'name':Js('/rosapi/get_param'),'serviceType':Js('rosapi/GetParam')})))
            var.put('request', var.get('ServiceRequest').create(Js({'name':var.get(u"this").get('name')})))
            @Js
            def PyJs_anonymous_154_(result, this, arguments, var=var):
                var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                var.registers(['value', 'result'])
                var.put('value', var.get('JSON').callprop('parse', var.get('result').get('value')))
                var.get('callback')(var.get('value'))
            PyJs_anonymous_154_._set_name('anonymous')
            var.get('paramClient').callprop('callService', var.get('request'), PyJs_anonymous_154_)
        PyJs_anonymous_153_._set_name('anonymous')
        var.get('Param').get('prototype').put('get', PyJs_anonymous_153_)
        @Js
        def PyJs_anonymous_155_(value, callback, this, arguments, var=var):
            var = Scope({'value':value, 'callback':callback, 'this':this, 'arguments':arguments}, var)
            var.registers(['callback', 'request', 'value', 'paramClient'])
            var.put('paramClient', var.get('Service').create(Js({'ros':var.get(u"this").get('ros'),'name':Js('/rosapi/set_param'),'serviceType':Js('rosapi/SetParam')})))
            var.put('request', var.get('ServiceRequest').create(Js({'name':var.get(u"this").get('name'),'value':var.get('JSON').callprop('stringify', var.get('value'))})))
            var.get('paramClient').callprop('callService', var.get('request'), var.get('callback'))
        PyJs_anonymous_155_._set_name('anonymous')
        var.get('Param').get('prototype').put('set', PyJs_anonymous_155_)
        @Js
        def PyJs_anonymous_156_(callback, this, arguments, var=var):
            var = Scope({'callback':callback, 'this':this, 'arguments':arguments}, var)
            var.registers(['callback', 'request', 'paramClient'])
            var.put('paramClient', var.get('Service').create(Js({'ros':var.get(u"this").get('ros'),'name':Js('/rosapi/delete_param'),'serviceType':Js('rosapi/DeleteParam')})))
            var.put('request', var.get('ServiceRequest').create(Js({'name':var.get(u"this").get('name')})))
            var.get('paramClient').callprop('callService', var.get('request'), var.get('callback'))
        PyJs_anonymous_156_._set_name('anonymous')
        var.get('Param').get('prototype').put('delete', PyJs_anonymous_156_)
        var.get('module').put('exports', var.get('Param'))
    PyJs_anonymous_152_._set_name('anonymous')
    @Js
    def PyJs_anonymous_157_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['socketAdapter', 'EventEmitter2', 'require', 'Ros', 'WebSocket', 'module', 'assign', 'WorkerSocket', 'Service', 'ServiceRequest', 'exports'])
        @Js
        def PyJsHoisted_Ros_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['that', 'options'])
            var.put('options', (var.get('options') or Js({})))
            var.put('that', var.get(u"this"))
            var.get(u"this").put('socket', var.get(u"null"))
            var.get(u"this").put('idCounter', Js(0.0))
            var.get(u"this").put('isConnected', Js(False))
            var.get(u"this").put('transportLibrary', (var.get('options').get('transportLibrary') or Js('websocket')))
            var.get(u"this").put('transportOptions', (var.get('options').get('transportOptions') or Js({})))
            @Js
            def PyJs_anonymous_158_(msg, this, arguments, var=var):
                var = Scope({'msg':msg, 'this':this, 'arguments':arguments}, var)
                var.registers(['msg'])
                var.get('that').callprop('sendEncodedMessage', var.get('msg'))
            PyJs_anonymous_158_._set_name('anonymous')
            var.get(u"this").put('_sendFunc', PyJs_anonymous_158_)
            if PyJsStrictEq(var.get('options').get('groovyCompatibility').typeof(),Js('undefined')):
                var.get(u"this").put('groovyCompatibility', Js(True))
            else:
                var.get(u"this").put('groovyCompatibility', var.get('options').get('groovyCompatibility'))
            var.get(u"this").callprop('setMaxListeners', Js(0.0))
            if var.get('options').get('url'):
                var.get(u"this").callprop('connect', var.get('options').get('url'))
        PyJsHoisted_Ros_.func_name = 'Ros'
        var.put('Ros', PyJsHoisted_Ros_)
        var.put('WebSocket', var.get('require')(Js('ws')))
        var.put('WorkerSocket', var.get('require')(Js('../util/workerSocket')))
        var.put('socketAdapter', var.get('require')(Js('./SocketAdapter.js')))
        var.put('Service', var.get('require')(Js('./Service')))
        var.put('ServiceRequest', var.get('require')(Js('./ServiceRequest')))
        var.put('assign', var.get('require')(Js('object-assign')))
        var.put('EventEmitter2', var.get('require')(Js('eventemitter2')).get('EventEmitter2'))
        pass
        var.get('Ros').get('prototype').put('__proto__', var.get('EventEmitter2').get('prototype'))
        @Js
        def PyJs_anonymous_159_(url, this, arguments, var=var):
            var = Scope({'url':url, 'this':this, 'arguments':arguments}, var)
            var.registers(['url', 'sock'])
            if PyJsStrictEq(var.get(u"this").get('transportLibrary'),Js('socket.io')):
                var.get(u"this").put('socket', var.get('assign')(var.get('io')(var.get('url'), Js({'force new connection':Js(True)})), var.get('socketAdapter')(var.get(u"this"))))
                var.get(u"this").get('socket').callprop('on', Js('connect'), var.get(u"this").get('socket').get('onopen'))
                var.get(u"this").get('socket').callprop('on', Js('data'), var.get(u"this").get('socket').get('onmessage'))
                var.get(u"this").get('socket').callprop('on', Js('close'), var.get(u"this").get('socket').get('onclose'))
                var.get(u"this").get('socket').callprop('on', Js('error'), var.get(u"this").get('socket').get('onerror'))
            else:
                if PyJsStrictEq(var.get(u"this").get('transportLibrary').get('constructor').get('name'),Js('RTCPeerConnection')):
                    var.get(u"this").put('socket', var.get('assign')(var.get(u"this").get('transportLibrary').callprop('createDataChannel', var.get('url'), var.get(u"this").get('transportOptions')), var.get('socketAdapter')(var.get(u"this"))))
                else:
                    if PyJsStrictEq(var.get(u"this").get('transportLibrary'),Js('websocket')):
                        if (var.get(u"this").get('socket').neg() or PyJsStrictEq(var.get(u"this").get('socket').get('readyState'),var.get('WebSocket').get('CLOSED'))):
                            var.put('sock', var.get('WebSocket').create(var.get('url')))
                            var.get('sock').put('binaryType', Js('arraybuffer'))
                            var.get(u"this").put('socket', var.get('assign')(var.get('sock'), var.get('socketAdapter')(var.get(u"this"))))
                    else:
                        if PyJsStrictEq(var.get(u"this").get('transportLibrary'),Js('workersocket')):
                            var.get(u"this").put('socket', var.get('assign')(var.get('WorkerSocket').create(var.get('url')), var.get('socketAdapter')(var.get(u"this"))))
                        else:
                            PyJsTempException = JsToPyException((Js('Unknown transportLibrary: ')+var.get(u"this").get('transportLibrary').callprop('toString')))
                            raise PyJsTempException
        PyJs_anonymous_159_._set_name('anonymous')
        var.get('Ros').get('prototype').put('connect', PyJs_anonymous_159_)
        @Js
        def PyJs_anonymous_160_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            if var.get(u"this").get('socket'):
                var.get(u"this").get('socket').callprop('close')
        PyJs_anonymous_160_._set_name('anonymous')
        var.get('Ros').get('prototype').put('close', PyJs_anonymous_160_)
        @Js
        def PyJs_anonymous_161_(mac, client, dest, rand, t, level, end, this, arguments, var=var):
            var = Scope({'mac':mac, 'client':client, 'dest':dest, 'rand':rand, 't':t, 'level':level, 'end':end, 'this':this, 'arguments':arguments}, var)
            var.registers(['rand', 't', 'level', 'mac', 'auth', 'dest', 'client', 'end'])
            var.put('auth', Js({'op':Js('auth'),'mac':var.get('mac'),'client':var.get('client'),'dest':var.get('dest'),'rand':var.get('rand'),'t':var.get('t'),'level':var.get('level'),'end':var.get('end')}))
            var.get(u"this").callprop('callOnConnection', var.get('auth'))
        PyJs_anonymous_161_._set_name('anonymous')
        var.get('Ros').get('prototype').put('authenticate', PyJs_anonymous_161_)
        @Js
        def PyJs_anonymous_162_(messageEncoded, this, arguments, var=var):
            var = Scope({'messageEncoded':messageEncoded, 'this':this, 'arguments':arguments}, var)
            var.registers(['that', 'messageEncoded', 'emitter'])
            var.put('emitter', var.get(u"null"))
            var.put('that', var.get(u"this"))
            if PyJsStrictEq(var.get(u"this").get('transportLibrary'),Js('socket.io')):
                @Js
                def PyJs_anonymous_163_(msg, this, arguments, var=var):
                    var = Scope({'msg':msg, 'this':this, 'arguments':arguments}, var)
                    var.registers(['msg'])
                    var.get('that').get('socket').callprop('emit', Js('operation'), var.get('msg'))
                PyJs_anonymous_163_._set_name('anonymous')
                var.put('emitter', PyJs_anonymous_163_)
            else:
                @Js
                def PyJs_anonymous_164_(msg, this, arguments, var=var):
                    var = Scope({'msg':msg, 'this':this, 'arguments':arguments}, var)
                    var.registers(['msg'])
                    var.get('that').get('socket').callprop('send', var.get('msg'))
                PyJs_anonymous_164_._set_name('anonymous')
                var.put('emitter', PyJs_anonymous_164_)
            if var.get(u"this").get('isConnected').neg():
                @Js
                def PyJs_anonymous_165_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    var.get('emitter')(var.get('messageEncoded'))
                PyJs_anonymous_165_._set_name('anonymous')
                var.get('that').callprop('once', Js('connection'), PyJs_anonymous_165_)
            else:
                var.get('emitter')(var.get('messageEncoded'))
        PyJs_anonymous_162_._set_name('anonymous')
        var.get('Ros').get('prototype').put('sendEncodedMessage', PyJs_anonymous_162_)
        @Js
        def PyJs_anonymous_166_(message, this, arguments, var=var):
            var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
            var.registers(['message'])
            if var.get(u"this").get('transportOptions').get('encoder'):
                var.get(u"this").get('transportOptions').callprop('encoder', var.get('message'), var.get(u"this").get('_sendFunc'))
            else:
                var.get(u"this").callprop('_sendFunc', var.get('JSON').callprop('stringify', var.get('message')))
        PyJs_anonymous_166_._set_name('anonymous')
        var.get('Ros').get('prototype').put('callOnConnection', PyJs_anonymous_166_)
        @Js
        def PyJs_anonymous_167_(level, id, this, arguments, var=var):
            var = Scope({'level':level, 'id':id, 'this':this, 'arguments':arguments}, var)
            var.registers(['levelMsg', 'level', 'id'])
            var.put('levelMsg', Js({'op':Js('set_level'),'level':var.get('level'),'id':var.get('id')}))
            var.get(u"this").callprop('callOnConnection', var.get('levelMsg'))
        PyJs_anonymous_167_._set_name('anonymous')
        var.get('Ros').get('prototype').put('setStatusLevel', PyJs_anonymous_167_)
        @Js
        def PyJs_anonymous_168_(callback, failedCallback, this, arguments, var=var):
            var = Scope({'callback':callback, 'failedCallback':failedCallback, 'this':this, 'arguments':arguments}, var)
            var.registers(['callback', 'failedCallback', 'request', 'getActionServers'])
            var.put('getActionServers', var.get('Service').create(Js({'ros':var.get(u"this"),'name':Js('/rosapi/action_servers'),'serviceType':Js('rosapi/GetActionServers')})))
            var.put('request', var.get('ServiceRequest').create(Js({})))
            if PyJsStrictEq(var.get('failedCallback',throw=False).typeof(),Js('function')):
                @Js
                def PyJs_anonymous_169_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('action_servers'))
                PyJs_anonymous_169_._set_name('anonymous')
                @Js
                def PyJs_anonymous_170_(message, this, arguments, var=var):
                    var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                    var.registers(['message'])
                    var.get('failedCallback')(var.get('message'))
                PyJs_anonymous_170_._set_name('anonymous')
                var.get('getActionServers').callprop('callService', var.get('request'), PyJs_anonymous_169_, PyJs_anonymous_170_)
            else:
                @Js
                def PyJs_anonymous_171_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('action_servers'))
                PyJs_anonymous_171_._set_name('anonymous')
                var.get('getActionServers').callprop('callService', var.get('request'), PyJs_anonymous_171_)
        PyJs_anonymous_168_._set_name('anonymous')
        var.get('Ros').get('prototype').put('getActionServers', PyJs_anonymous_168_)
        @Js
        def PyJs_anonymous_172_(callback, failedCallback, this, arguments, var=var):
            var = Scope({'callback':callback, 'failedCallback':failedCallback, 'this':this, 'arguments':arguments}, var)
            var.registers(['callback', 'failedCallback', 'request', 'topicsClient'])
            var.put('topicsClient', var.get('Service').create(Js({'ros':var.get(u"this"),'name':Js('/rosapi/topics'),'serviceType':Js('rosapi/Topics')})))
            var.put('request', var.get('ServiceRequest').create())
            if PyJsStrictEq(var.get('failedCallback',throw=False).typeof(),Js('function')):
                @Js
                def PyJs_anonymous_173_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result'))
                PyJs_anonymous_173_._set_name('anonymous')
                @Js
                def PyJs_anonymous_174_(message, this, arguments, var=var):
                    var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                    var.registers(['message'])
                    var.get('failedCallback')(var.get('message'))
                PyJs_anonymous_174_._set_name('anonymous')
                var.get('topicsClient').callprop('callService', var.get('request'), PyJs_anonymous_173_, PyJs_anonymous_174_)
            else:
                @Js
                def PyJs_anonymous_175_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result'))
                PyJs_anonymous_175_._set_name('anonymous')
                var.get('topicsClient').callprop('callService', var.get('request'), PyJs_anonymous_175_)
        PyJs_anonymous_172_._set_name('anonymous')
        var.get('Ros').get('prototype').put('getTopics', PyJs_anonymous_172_)
        @Js
        def PyJs_anonymous_176_(topicType, callback, failedCallback, this, arguments, var=var):
            var = Scope({'topicType':topicType, 'callback':callback, 'failedCallback':failedCallback, 'this':this, 'arguments':arguments}, var)
            var.registers(['topicsForTypeClient', 'failedCallback', 'callback', 'topicType', 'request'])
            var.put('topicsForTypeClient', var.get('Service').create(Js({'ros':var.get(u"this"),'name':Js('/rosapi/topics_for_type'),'serviceType':Js('rosapi/TopicsForType')})))
            var.put('request', var.get('ServiceRequest').create(Js({'type':var.get('topicType')})))
            if PyJsStrictEq(var.get('failedCallback',throw=False).typeof(),Js('function')):
                @Js
                def PyJs_anonymous_177_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('topics'))
                PyJs_anonymous_177_._set_name('anonymous')
                @Js
                def PyJs_anonymous_178_(message, this, arguments, var=var):
                    var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                    var.registers(['message'])
                    var.get('failedCallback')(var.get('message'))
                PyJs_anonymous_178_._set_name('anonymous')
                var.get('topicsForTypeClient').callprop('callService', var.get('request'), PyJs_anonymous_177_, PyJs_anonymous_178_)
            else:
                @Js
                def PyJs_anonymous_179_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('topics'))
                PyJs_anonymous_179_._set_name('anonymous')
                var.get('topicsForTypeClient').callprop('callService', var.get('request'), PyJs_anonymous_179_)
        PyJs_anonymous_176_._set_name('anonymous')
        var.get('Ros').get('prototype').put('getTopicsForType', PyJs_anonymous_176_)
        @Js
        def PyJs_anonymous_180_(callback, failedCallback, this, arguments, var=var):
            var = Scope({'callback':callback, 'failedCallback':failedCallback, 'this':this, 'arguments':arguments}, var)
            var.registers(['callback', 'failedCallback', 'request', 'servicesClient'])
            var.put('servicesClient', var.get('Service').create(Js({'ros':var.get(u"this"),'name':Js('/rosapi/services'),'serviceType':Js('rosapi/Services')})))
            var.put('request', var.get('ServiceRequest').create())
            if PyJsStrictEq(var.get('failedCallback',throw=False).typeof(),Js('function')):
                @Js
                def PyJs_anonymous_181_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('services'))
                PyJs_anonymous_181_._set_name('anonymous')
                @Js
                def PyJs_anonymous_182_(message, this, arguments, var=var):
                    var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                    var.registers(['message'])
                    var.get('failedCallback')(var.get('message'))
                PyJs_anonymous_182_._set_name('anonymous')
                var.get('servicesClient').callprop('callService', var.get('request'), PyJs_anonymous_181_, PyJs_anonymous_182_)
            else:
                @Js
                def PyJs_anonymous_183_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('services'))
                PyJs_anonymous_183_._set_name('anonymous')
                var.get('servicesClient').callprop('callService', var.get('request'), PyJs_anonymous_183_)
        PyJs_anonymous_180_._set_name('anonymous')
        var.get('Ros').get('prototype').put('getServices', PyJs_anonymous_180_)
        @Js
        def PyJs_anonymous_184_(serviceType, callback, failedCallback, this, arguments, var=var):
            var = Scope({'serviceType':serviceType, 'callback':callback, 'failedCallback':failedCallback, 'this':this, 'arguments':arguments}, var)
            var.registers(['servicesForTypeClient', 'serviceType', 'failedCallback', 'callback', 'request'])
            var.put('servicesForTypeClient', var.get('Service').create(Js({'ros':var.get(u"this"),'name':Js('/rosapi/services_for_type'),'serviceType':Js('rosapi/ServicesForType')})))
            var.put('request', var.get('ServiceRequest').create(Js({'type':var.get('serviceType')})))
            if PyJsStrictEq(var.get('failedCallback',throw=False).typeof(),Js('function')):
                @Js
                def PyJs_anonymous_185_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('services'))
                PyJs_anonymous_185_._set_name('anonymous')
                @Js
                def PyJs_anonymous_186_(message, this, arguments, var=var):
                    var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                    var.registers(['message'])
                    var.get('failedCallback')(var.get('message'))
                PyJs_anonymous_186_._set_name('anonymous')
                var.get('servicesForTypeClient').callprop('callService', var.get('request'), PyJs_anonymous_185_, PyJs_anonymous_186_)
            else:
                @Js
                def PyJs_anonymous_187_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('services'))
                PyJs_anonymous_187_._set_name('anonymous')
                var.get('servicesForTypeClient').callprop('callService', var.get('request'), PyJs_anonymous_187_)
        PyJs_anonymous_184_._set_name('anonymous')
        var.get('Ros').get('prototype').put('getServicesForType', PyJs_anonymous_184_)
        @Js
        def PyJs_anonymous_188_(type, callback, failedCallback, this, arguments, var=var):
            var = Scope({'type':type, 'callback':callback, 'failedCallback':failedCallback, 'this':this, 'arguments':arguments}, var)
            var.registers(['serviceTypeClient', 'failedCallback', 'type', 'callback', 'request'])
            var.put('serviceTypeClient', var.get('Service').create(Js({'ros':var.get(u"this"),'name':Js('/rosapi/service_request_details'),'serviceType':Js('rosapi/ServiceRequestDetails')})))
            var.put('request', var.get('ServiceRequest').create(Js({'type':var.get('type')})))
            if PyJsStrictEq(var.get('failedCallback',throw=False).typeof(),Js('function')):
                @Js
                def PyJs_anonymous_189_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result'))
                PyJs_anonymous_189_._set_name('anonymous')
                @Js
                def PyJs_anonymous_190_(message, this, arguments, var=var):
                    var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                    var.registers(['message'])
                    var.get('failedCallback')(var.get('message'))
                PyJs_anonymous_190_._set_name('anonymous')
                var.get('serviceTypeClient').callprop('callService', var.get('request'), PyJs_anonymous_189_, PyJs_anonymous_190_)
            else:
                @Js
                def PyJs_anonymous_191_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result'))
                PyJs_anonymous_191_._set_name('anonymous')
                var.get('serviceTypeClient').callprop('callService', var.get('request'), PyJs_anonymous_191_)
        PyJs_anonymous_188_._set_name('anonymous')
        var.get('Ros').get('prototype').put('getServiceRequestDetails', PyJs_anonymous_188_)
        @Js
        def PyJs_anonymous_192_(type, callback, failedCallback, this, arguments, var=var):
            var = Scope({'type':type, 'callback':callback, 'failedCallback':failedCallback, 'this':this, 'arguments':arguments}, var)
            var.registers(['serviceTypeClient', 'failedCallback', 'type', 'callback', 'request'])
            var.put('serviceTypeClient', var.get('Service').create(Js({'ros':var.get(u"this"),'name':Js('/rosapi/service_response_details'),'serviceType':Js('rosapi/ServiceResponseDetails')})))
            var.put('request', var.get('ServiceRequest').create(Js({'type':var.get('type')})))
            if PyJsStrictEq(var.get('failedCallback',throw=False).typeof(),Js('function')):
                @Js
                def PyJs_anonymous_193_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result'))
                PyJs_anonymous_193_._set_name('anonymous')
                @Js
                def PyJs_anonymous_194_(message, this, arguments, var=var):
                    var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                    var.registers(['message'])
                    var.get('failedCallback')(var.get('message'))
                PyJs_anonymous_194_._set_name('anonymous')
                var.get('serviceTypeClient').callprop('callService', var.get('request'), PyJs_anonymous_193_, PyJs_anonymous_194_)
            else:
                @Js
                def PyJs_anonymous_195_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result'))
                PyJs_anonymous_195_._set_name('anonymous')
                var.get('serviceTypeClient').callprop('callService', var.get('request'), PyJs_anonymous_195_)
        PyJs_anonymous_192_._set_name('anonymous')
        var.get('Ros').get('prototype').put('getServiceResponseDetails', PyJs_anonymous_192_)
        @Js
        def PyJs_anonymous_196_(callback, failedCallback, this, arguments, var=var):
            var = Scope({'callback':callback, 'failedCallback':failedCallback, 'this':this, 'arguments':arguments}, var)
            var.registers(['callback', 'nodesClient', 'request', 'failedCallback'])
            var.put('nodesClient', var.get('Service').create(Js({'ros':var.get(u"this"),'name':Js('/rosapi/nodes'),'serviceType':Js('rosapi/Nodes')})))
            var.put('request', var.get('ServiceRequest').create())
            if PyJsStrictEq(var.get('failedCallback',throw=False).typeof(),Js('function')):
                @Js
                def PyJs_anonymous_197_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('nodes'))
                PyJs_anonymous_197_._set_name('anonymous')
                @Js
                def PyJs_anonymous_198_(message, this, arguments, var=var):
                    var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                    var.registers(['message'])
                    var.get('failedCallback')(var.get('message'))
                PyJs_anonymous_198_._set_name('anonymous')
                var.get('nodesClient').callprop('callService', var.get('request'), PyJs_anonymous_197_, PyJs_anonymous_198_)
            else:
                @Js
                def PyJs_anonymous_199_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('nodes'))
                PyJs_anonymous_199_._set_name('anonymous')
                var.get('nodesClient').callprop('callService', var.get('request'), PyJs_anonymous_199_)
        PyJs_anonymous_196_._set_name('anonymous')
        var.get('Ros').get('prototype').put('getNodes', PyJs_anonymous_196_)
        @Js
        def PyJs_anonymous_200_(node, callback, failedCallback, this, arguments, var=var):
            var = Scope({'node':node, 'callback':callback, 'failedCallback':failedCallback, 'this':this, 'arguments':arguments}, var)
            var.registers(['node', 'nodesClient', 'failedCallback', 'callback', 'request'])
            var.put('nodesClient', var.get('Service').create(Js({'ros':var.get(u"this"),'name':Js('/rosapi/node_details'),'serviceType':Js('rosapi/NodeDetails')})))
            var.put('request', var.get('ServiceRequest').create(Js({'node':var.get('node')})))
            if PyJsStrictEq(var.get('failedCallback',throw=False).typeof(),Js('function')):
                @Js
                def PyJs_anonymous_201_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('subscribing'), var.get('result').get('publishing'), var.get('result').get('services'))
                PyJs_anonymous_201_._set_name('anonymous')
                @Js
                def PyJs_anonymous_202_(message, this, arguments, var=var):
                    var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                    var.registers(['message'])
                    var.get('failedCallback')(var.get('message'))
                PyJs_anonymous_202_._set_name('anonymous')
                var.get('nodesClient').callprop('callService', var.get('request'), PyJs_anonymous_201_, PyJs_anonymous_202_)
            else:
                @Js
                def PyJs_anonymous_203_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result'))
                PyJs_anonymous_203_._set_name('anonymous')
                var.get('nodesClient').callprop('callService', var.get('request'), PyJs_anonymous_203_)
        PyJs_anonymous_200_._set_name('anonymous')
        var.get('Ros').get('prototype').put('getNodeDetails', PyJs_anonymous_200_)
        @Js
        def PyJs_anonymous_204_(callback, failedCallback, this, arguments, var=var):
            var = Scope({'callback':callback, 'failedCallback':failedCallback, 'this':this, 'arguments':arguments}, var)
            var.registers(['callback', 'failedCallback', 'request', 'paramsClient'])
            var.put('paramsClient', var.get('Service').create(Js({'ros':var.get(u"this"),'name':Js('/rosapi/get_param_names'),'serviceType':Js('rosapi/GetParamNames')})))
            var.put('request', var.get('ServiceRequest').create())
            if PyJsStrictEq(var.get('failedCallback',throw=False).typeof(),Js('function')):
                @Js
                def PyJs_anonymous_205_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('names'))
                PyJs_anonymous_205_._set_name('anonymous')
                @Js
                def PyJs_anonymous_206_(message, this, arguments, var=var):
                    var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                    var.registers(['message'])
                    var.get('failedCallback')(var.get('message'))
                PyJs_anonymous_206_._set_name('anonymous')
                var.get('paramsClient').callprop('callService', var.get('request'), PyJs_anonymous_205_, PyJs_anonymous_206_)
            else:
                @Js
                def PyJs_anonymous_207_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('names'))
                PyJs_anonymous_207_._set_name('anonymous')
                var.get('paramsClient').callprop('callService', var.get('request'), PyJs_anonymous_207_)
        PyJs_anonymous_204_._set_name('anonymous')
        var.get('Ros').get('prototype').put('getParams', PyJs_anonymous_204_)
        @Js
        def PyJs_anonymous_208_(topic, callback, failedCallback, this, arguments, var=var):
            var = Scope({'topic':topic, 'callback':callback, 'failedCallback':failedCallback, 'this':this, 'arguments':arguments}, var)
            var.registers(['topicTypeClient', 'failedCallback', 'topic', 'callback', 'request'])
            var.put('topicTypeClient', var.get('Service').create(Js({'ros':var.get(u"this"),'name':Js('/rosapi/topic_type'),'serviceType':Js('rosapi/TopicType')})))
            var.put('request', var.get('ServiceRequest').create(Js({'topic':var.get('topic')})))
            if PyJsStrictEq(var.get('failedCallback',throw=False).typeof(),Js('function')):
                @Js
                def PyJs_anonymous_209_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('type'))
                PyJs_anonymous_209_._set_name('anonymous')
                @Js
                def PyJs_anonymous_210_(message, this, arguments, var=var):
                    var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                    var.registers(['message'])
                    var.get('failedCallback')(var.get('message'))
                PyJs_anonymous_210_._set_name('anonymous')
                var.get('topicTypeClient').callprop('callService', var.get('request'), PyJs_anonymous_209_, PyJs_anonymous_210_)
            else:
                @Js
                def PyJs_anonymous_211_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('type'))
                PyJs_anonymous_211_._set_name('anonymous')
                var.get('topicTypeClient').callprop('callService', var.get('request'), PyJs_anonymous_211_)
        PyJs_anonymous_208_._set_name('anonymous')
        var.get('Ros').get('prototype').put('getTopicType', PyJs_anonymous_208_)
        @Js
        def PyJs_anonymous_212_(service, callback, failedCallback, this, arguments, var=var):
            var = Scope({'service':service, 'callback':callback, 'failedCallback':failedCallback, 'this':this, 'arguments':arguments}, var)
            var.registers(['serviceTypeClient', 'service', 'failedCallback', 'callback', 'request'])
            var.put('serviceTypeClient', var.get('Service').create(Js({'ros':var.get(u"this"),'name':Js('/rosapi/service_type'),'serviceType':Js('rosapi/ServiceType')})))
            var.put('request', var.get('ServiceRequest').create(Js({'service':var.get('service')})))
            if PyJsStrictEq(var.get('failedCallback',throw=False).typeof(),Js('function')):
                @Js
                def PyJs_anonymous_213_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('type'))
                PyJs_anonymous_213_._set_name('anonymous')
                @Js
                def PyJs_anonymous_214_(message, this, arguments, var=var):
                    var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                    var.registers(['message'])
                    var.get('failedCallback')(var.get('message'))
                PyJs_anonymous_214_._set_name('anonymous')
                var.get('serviceTypeClient').callprop('callService', var.get('request'), PyJs_anonymous_213_, PyJs_anonymous_214_)
            else:
                @Js
                def PyJs_anonymous_215_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('type'))
                PyJs_anonymous_215_._set_name('anonymous')
                var.get('serviceTypeClient').callprop('callService', var.get('request'), PyJs_anonymous_215_)
        PyJs_anonymous_212_._set_name('anonymous')
        var.get('Ros').get('prototype').put('getServiceType', PyJs_anonymous_212_)
        @Js
        def PyJs_anonymous_216_(message, callback, failedCallback, this, arguments, var=var):
            var = Scope({'message':message, 'callback':callback, 'failedCallback':failedCallback, 'this':this, 'arguments':arguments}, var)
            var.registers(['messageDetailClient', 'failedCallback', 'callback', 'request', 'message'])
            var.put('messageDetailClient', var.get('Service').create(Js({'ros':var.get(u"this"),'name':Js('/rosapi/message_details'),'serviceType':Js('rosapi/MessageDetails')})))
            var.put('request', var.get('ServiceRequest').create(Js({'type':var.get('message')})))
            if PyJsStrictEq(var.get('failedCallback',throw=False).typeof(),Js('function')):
                @Js
                def PyJs_anonymous_217_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('typedefs'))
                PyJs_anonymous_217_._set_name('anonymous')
                @Js
                def PyJs_anonymous_218_(message, this, arguments, var=var):
                    var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                    var.registers(['message'])
                    var.get('failedCallback')(var.get('message'))
                PyJs_anonymous_218_._set_name('anonymous')
                var.get('messageDetailClient').callprop('callService', var.get('request'), PyJs_anonymous_217_, PyJs_anonymous_218_)
            else:
                @Js
                def PyJs_anonymous_219_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result').get('typedefs'))
                PyJs_anonymous_219_._set_name('anonymous')
                var.get('messageDetailClient').callprop('callService', var.get('request'), PyJs_anonymous_219_)
        PyJs_anonymous_216_._set_name('anonymous')
        var.get('Ros').get('prototype').put('getMessageDetails', PyJs_anonymous_216_)
        @Js
        def PyJs_anonymous_220_(defs, this, arguments, var=var):
            var = Scope({'defs':defs, 'this':this, 'arguments':arguments}, var)
            var.registers(['that', 'decodeTypeDefsRec', 'defs'])
            var.put('that', var.get(u"this"))
            @Js
            def PyJs_anonymous_221_(theType, hints, this, arguments, var=var):
                var = Scope({'theType':theType, 'hints':hints, 'this':this, 'arguments':arguments}, var)
                var.registers(['fieldName', 'j', 'fieldType', 'hints', 'typeDefDict', 'theType', 'arrayLen', 'i', 'subResult', 'sub'])
                var.put('typeDefDict', Js({}))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('theType').get('fieldnames').get('length')):
                    try:
                        var.put('arrayLen', var.get('theType').get('fieldarraylen').get(var.get('i')))
                        var.put('fieldName', var.get('theType').get('fieldnames').get(var.get('i')))
                        var.put('fieldType', var.get('theType').get('fieldtypes').get(var.get('i')))
                        if PyJsStrictEq(var.get('fieldType').callprop('indexOf', Js('/')),(-Js(1.0))):
                            if PyJsStrictEq(var.get('arrayLen'),(-Js(1.0))):
                                var.get('typeDefDict').put(var.get('fieldName'), var.get('fieldType'))
                            else:
                                var.get('typeDefDict').put(var.get('fieldName'), Js([var.get('fieldType')]))
                        else:
                            var.put('sub', Js(False))
                            #for JS loop
                            var.put('j', Js(0.0))
                            while (var.get('j')<var.get('hints').get('length')):
                                try:
                                    if PyJsStrictEq(var.get('hints').get(var.get('j')).get('type').callprop('toString'),var.get('fieldType').callprop('toString')):
                                        var.put('sub', var.get('hints').get(var.get('j')))
                                        break
                                finally:
                                        (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                            if var.get('sub'):
                                var.put('subResult', var.get('decodeTypeDefsRec')(var.get('sub'), var.get('hints')))
                                if PyJsStrictEq(var.get('arrayLen'),(-Js(1.0))):
                                    pass
                                else:
                                    var.get('typeDefDict').put(var.get('fieldName'), Js([var.get('subResult')]))
                            else:
                                var.get('that').callprop('emit', Js('error'), ((Js('Cannot find ')+var.get('fieldType'))+Js(' in decodeTypeDefs')))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                return var.get('typeDefDict')
            PyJs_anonymous_221_._set_name('anonymous')
            var.put('decodeTypeDefsRec', PyJs_anonymous_221_)
            return var.get('decodeTypeDefsRec')(var.get('defs').get('0'), var.get('defs'))
        PyJs_anonymous_220_._set_name('anonymous')
        var.get('Ros').get('prototype').put('decodeTypeDefs', PyJs_anonymous_220_)
        @Js
        def PyJs_anonymous_222_(callback, failedCallback, this, arguments, var=var):
            var = Scope({'callback':callback, 'failedCallback':failedCallback, 'this':this, 'arguments':arguments}, var)
            var.registers(['callback', 'failedCallback', 'request', 'topicsAndRawTypesClient'])
            var.put('topicsAndRawTypesClient', var.get('Service').create(Js({'ros':var.get(u"this"),'name':Js('/rosapi/topics_and_raw_types'),'serviceType':Js('rosapi/TopicsAndRawTypes')})))
            var.put('request', var.get('ServiceRequest').create())
            if PyJsStrictEq(var.get('failedCallback',throw=False).typeof(),Js('function')):
                @Js
                def PyJs_anonymous_223_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result'))
                PyJs_anonymous_223_._set_name('anonymous')
                @Js
                def PyJs_anonymous_224_(message, this, arguments, var=var):
                    var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                    var.registers(['message'])
                    var.get('failedCallback')(var.get('message'))
                PyJs_anonymous_224_._set_name('anonymous')
                var.get('topicsAndRawTypesClient').callprop('callService', var.get('request'), PyJs_anonymous_223_, PyJs_anonymous_224_)
            else:
                @Js
                def PyJs_anonymous_225_(result, this, arguments, var=var):
                    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['result'])
                    var.get('callback')(var.get('result'))
                PyJs_anonymous_225_._set_name('anonymous')
                var.get('topicsAndRawTypesClient').callprop('callService', var.get('request'), PyJs_anonymous_225_)
        PyJs_anonymous_222_._set_name('anonymous')
        var.get('Ros').get('prototype').put('getTopicsAndRawTypes', PyJs_anonymous_222_)
        var.get('module').put('exports', var.get('Ros'))
    PyJs_anonymous_157_._set_name('anonymous')
    @Js
    def PyJs_anonymous_226_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['EventEmitter2', 'require', 'ServiceResponse', 'module', 'Service', 'ServiceRequest', 'exports'])
        @Js
        def PyJsHoisted_Service_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['options'])
            var.put('options', (var.get('options') or Js({})))
            var.get(u"this").put('ros', var.get('options').get('ros'))
            var.get(u"this").put('name', var.get('options').get('name'))
            var.get(u"this").put('serviceType', var.get('options').get('serviceType'))
            var.get(u"this").put('isAdvertised', Js(False))
            var.get(u"this").put('_serviceCallback', var.get(u"null"))
        PyJsHoisted_Service_.func_name = 'Service'
        var.put('Service', PyJsHoisted_Service_)
        var.put('ServiceResponse', var.get('require')(Js('./ServiceResponse')))
        var.put('ServiceRequest', var.get('require')(Js('./ServiceRequest')))
        var.put('EventEmitter2', var.get('require')(Js('eventemitter2')).get('EventEmitter2'))
        pass
        var.get('Service').get('prototype').put('__proto__', var.get('EventEmitter2').get('prototype'))
        @Js
        def PyJs_anonymous_227_(request, callback, failedCallback, this, arguments, var=var):
            var = Scope({'request':request, 'callback':callback, 'failedCallback':failedCallback, 'this':this, 'arguments':arguments}, var)
            var.registers(['serviceCallId', 'call', 'failedCallback', 'callback', 'request'])
            if var.get(u"this").get('isAdvertised'):
                return var.get('undefined')
            var.put('serviceCallId', (((Js('call_service:')+var.get(u"this").get('name'))+Js(':'))+var.get(u"this").get('ros').put('idCounter',Js(var.get(u"this").get('ros').get('idCounter').to_number())+Js(1))))
            if (var.get('callback') or var.get('failedCallback')):
                @Js
                def PyJs_anonymous_228_(message, this, arguments, var=var):
                    var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                    var.registers(['message'])
                    if (PyJsStrictNeq(var.get('message').get('result'),var.get('undefined')) and PyJsStrictEq(var.get('message').get('result'),Js(False))):
                        if PyJsStrictEq(var.get('failedCallback',throw=False).typeof(),Js('function')):
                            var.get('failedCallback')(var.get('message').get('values'))
                    else:
                        if PyJsStrictEq(var.get('callback',throw=False).typeof(),Js('function')):
                            var.get('callback')(var.get('ServiceResponse').create(var.get('message').get('values')))
                PyJs_anonymous_228_._set_name('anonymous')
                var.get(u"this").get('ros').callprop('once', var.get('serviceCallId'), PyJs_anonymous_228_)
            var.put('call', Js({'op':Js('call_service'),'id':var.get('serviceCallId'),'service':var.get(u"this").get('name'),'type':var.get(u"this").get('serviceType'),'args':var.get('request')}))
            var.get(u"this").get('ros').callprop('callOnConnection', var.get('call'))
        PyJs_anonymous_227_._set_name('anonymous')
        var.get('Service').get('prototype').put('callService', PyJs_anonymous_227_)
        @Js
        def PyJs_anonymous_229_(callback, this, arguments, var=var):
            var = Scope({'callback':callback, 'this':this, 'arguments':arguments}, var)
            var.registers(['callback'])
            if (var.get(u"this").get('isAdvertised') or PyJsStrictNeq(var.get('callback',throw=False).typeof(),Js('function'))):
                return var.get('undefined')
            var.get(u"this").put('_serviceCallback', var.get('callback'))
            var.get(u"this").get('ros').callprop('on', var.get(u"this").get('name'), var.get(u"this").get('_serviceResponse').callprop('bind', var.get(u"this")))
            var.get(u"this").get('ros').callprop('callOnConnection', Js({'op':Js('advertise_service'),'type':var.get(u"this").get('serviceType'),'service':var.get(u"this").get('name')}))
            var.get(u"this").put('isAdvertised', Js(True))
        PyJs_anonymous_229_._set_name('anonymous')
        var.get('Service').get('prototype').put('advertise', PyJs_anonymous_229_)
        @Js
        def PyJs_anonymous_230_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            if var.get(u"this").get('isAdvertised').neg():
                return var.get('undefined')
            var.get(u"this").get('ros').callprop('callOnConnection', Js({'op':Js('unadvertise_service'),'service':var.get(u"this").get('name')}))
            var.get(u"this").put('isAdvertised', Js(False))
        PyJs_anonymous_230_._set_name('anonymous')
        var.get('Service').get('prototype').put('unadvertise', PyJs_anonymous_230_)
        @Js
        def PyJs_anonymous_231_(rosbridgeRequest, this, arguments, var=var):
            var = Scope({'rosbridgeRequest':rosbridgeRequest, 'this':this, 'arguments':arguments}, var)
            var.registers(['success', 'response', 'call', 'rosbridgeRequest'])
            var.put('response', Js({}))
            var.put('success', var.get(u"this").callprop('_serviceCallback', var.get('rosbridgeRequest').get('args'), var.get('response')))
            var.put('call', Js({'op':Js('service_response'),'service':var.get(u"this").get('name'),'values':var.get('ServiceResponse').create(var.get('response')),'result':var.get('success')}))
            if var.get('rosbridgeRequest').get('id'):
                var.get('call').put('id', var.get('rosbridgeRequest').get('id'))
            var.get(u"this").get('ros').callprop('callOnConnection', var.get('call'))
        PyJs_anonymous_231_._set_name('anonymous')
        var.get('Service').get('prototype').put('_serviceResponse', PyJs_anonymous_231_)
        var.get('module').put('exports', var.get('Service'))
    PyJs_anonymous_226_._set_name('anonymous')
    @Js
    def PyJs_anonymous_232_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['require', 'module', 'assign', 'ServiceRequest', 'exports'])
        @Js
        def PyJsHoisted_ServiceRequest_(values, this, arguments, var=var):
            var = Scope({'values':values, 'this':this, 'arguments':arguments}, var)
            var.registers(['values'])
            var.get('assign')(var.get(u"this"), var.get('values'))
        PyJsHoisted_ServiceRequest_.func_name = 'ServiceRequest'
        var.put('ServiceRequest', PyJsHoisted_ServiceRequest_)
        var.put('assign', var.get('require')(Js('object-assign')))
        pass
        var.get('module').put('exports', var.get('ServiceRequest'))
    PyJs_anonymous_232_._set_name('anonymous')
    @Js
    def PyJs_anonymous_233_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['require', 'ServiceResponse', 'module', 'assign', 'exports'])
        @Js
        def PyJsHoisted_ServiceResponse_(values, this, arguments, var=var):
            var = Scope({'values':values, 'this':this, 'arguments':arguments}, var)
            var.registers(['values'])
            var.get('assign')(var.get(u"this"), var.get('values'))
        PyJsHoisted_ServiceResponse_.func_name = 'ServiceResponse'
        var.put('ServiceResponse', PyJsHoisted_ServiceResponse_)
        var.put('assign', var.get('require')(Js('object-assign')))
        pass
        var.get('module').put('exports', var.get('ServiceResponse'))
    PyJs_anonymous_233_._set_name('anonymous')
    @Js
    def PyJs_anonymous_234_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['BSON', 'SocketAdapter', 'decompressPng', 'require', 'module', 'typedArrayTagger', 'CBOR', 'exports'])
        @Js
        def PyJsHoisted_SocketAdapter_(client, this, arguments, var=var):
            var = Scope({'client':client, 'this':this, 'arguments':arguments}, var)
            var.registers(['decodeBSON', 'handleMessage', 'decoder', 'handlePng', 'client'])
            @Js
            def PyJsHoisted_handleMessage_(message, this, arguments, var=var):
                var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                var.registers(['message'])
                if PyJsStrictEq(var.get('message').get('op'),Js('publish')):
                    var.get('client').callprop('emit', var.get('message').get('topic'), var.get('message').get('msg'))
                else:
                    if PyJsStrictEq(var.get('message').get('op'),Js('service_response')):
                        var.get('client').callprop('emit', var.get('message').get('id'), var.get('message'))
                    else:
                        if PyJsStrictEq(var.get('message').get('op'),Js('call_service')):
                            var.get('client').callprop('emit', var.get('message').get('service'), var.get('message'))
                        else:
                            if PyJsStrictEq(var.get('message').get('op'),Js('status')):
                                if var.get('message').get('id'):
                                    var.get('client').callprop('emit', (Js('status:')+var.get('message').get('id')), var.get('message'))
                                else:
                                    var.get('client').callprop('emit', Js('status'), var.get('message'))
            PyJsHoisted_handleMessage_.func_name = 'handleMessage'
            var.put('handleMessage', PyJsHoisted_handleMessage_)
            @Js
            def PyJsHoisted_handlePng_(message, callback, this, arguments, var=var):
                var = Scope({'message':message, 'callback':callback, 'this':this, 'arguments':arguments}, var)
                var.registers(['callback', 'message'])
                if PyJsStrictEq(var.get('message').get('op'),Js('png')):
                    var.get('decompressPng')(var.get('message').get('data'), var.get('callback'))
                else:
                    var.get('callback')(var.get('message'))
            PyJsHoisted_handlePng_.func_name = 'handlePng'
            var.put('handlePng', PyJsHoisted_handlePng_)
            @Js
            def PyJsHoisted_decodeBSON_(data, callback, this, arguments, var=var):
                var = Scope({'data':data, 'callback':callback, 'this':this, 'arguments':arguments}, var)
                var.registers(['reader', 'callback', 'data'])
                if var.get('BSON').neg():
                    PyJsTempException = JsToPyException(Js('Cannot process BSON encoded message without BSON header.'))
                    raise PyJsTempException
                var.put('reader', var.get('FileReader').create())
                @Js
                def PyJs_anonymous_235_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers(['msg', 'uint8Array'])
                    var.put('uint8Array', var.get('Uint8Array').create(var.get(u"this").get('result')))
                    var.put('msg', var.get('BSON').callprop('deserialize', var.get('uint8Array')))
                    var.get('callback')(var.get('msg'))
                PyJs_anonymous_235_._set_name('anonymous')
                var.get('reader').put('onload', PyJs_anonymous_235_)
                var.get('reader').callprop('readAsArrayBuffer', var.get('data'))
            PyJsHoisted_decodeBSON_.func_name = 'decodeBSON'
            var.put('decodeBSON', PyJsHoisted_decodeBSON_)
            var.put('decoder', var.get(u"null"))
            if var.get('client').get('transportOptions').get('decoder'):
                var.put('decoder', var.get('client').get('transportOptions').get('decoder'))
            pass
            pass
            pass
            @Js
            def PyJs_onOpen_236_(event, this, arguments, var=var):
                var = Scope({'event':event, 'this':this, 'arguments':arguments, 'onOpen':PyJs_onOpen_236_}, var)
                var.registers(['event'])
                var.get('client').put('isConnected', Js(True))
                var.get('client').callprop('emit', Js('connection'), var.get('event'))
            PyJs_onOpen_236_._set_name('onOpen')
            @Js
            def PyJs_onClose_237_(event, this, arguments, var=var):
                var = Scope({'event':event, 'this':this, 'arguments':arguments, 'onClose':PyJs_onClose_237_}, var)
                var.registers(['event'])
                var.get('client').put('isConnected', Js(False))
                var.get('client').callprop('emit', Js('close'), var.get('event'))
            PyJs_onClose_237_._set_name('onClose')
            @Js
            def PyJs_onError_238_(event, this, arguments, var=var):
                var = Scope({'event':event, 'this':this, 'arguments':arguments, 'onError':PyJs_onError_238_}, var)
                var.registers(['event'])
                var.get('client').callprop('emit', Js('error'), var.get('event'))
            PyJs_onError_238_._set_name('onError')
            @Js
            def PyJs_onMessage_239_(data, this, arguments, var=var):
                var = Scope({'data':data, 'this':this, 'arguments':arguments, 'onMessage':PyJs_onMessage_239_}, var)
                var.registers(['data', 'decoded', 'message'])
                if var.get('decoder'):
                    @Js
                    def PyJs_anonymous_240_(message, this, arguments, var=var):
                        var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                        var.registers(['message'])
                        var.get('handleMessage')(var.get('message'))
                    PyJs_anonymous_240_._set_name('anonymous')
                    var.get('decoder')(var.get('data').get('data'), PyJs_anonymous_240_)
                else:
                    if (PyJsStrictNeq(var.get('Blob',throw=False).typeof(),Js('undefined')) and var.get('data').get('data').instanceof(var.get('Blob'))):
                        @Js
                        def PyJs_anonymous_241_(message, this, arguments, var=var):
                            var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                            var.registers(['message'])
                            var.get('handlePng')(var.get('message'), var.get('handleMessage'))
                        PyJs_anonymous_241_._set_name('anonymous')
                        var.get('decodeBSON')(var.get('data').get('data'), PyJs_anonymous_241_)
                    else:
                        if var.get('data').get('data').instanceof(var.get('ArrayBuffer')):
                            var.put('decoded', var.get('CBOR').callprop('decode', var.get('data').get('data'), var.get('typedArrayTagger')))
                            var.get('handleMessage')(var.get('decoded'))
                        else:
                            var.put('message', var.get('JSON').callprop('parse', (var.get('data') if PyJsStrictEq(var.get('data',throw=False).typeof(),Js('string')) else var.get('data').get('data'))))
                            var.get('handlePng')(var.get('message'), var.get('handleMessage'))
            PyJs_onMessage_239_._set_name('onMessage')
            return Js({'onopen':PyJs_onOpen_236_,'onclose':PyJs_onClose_237_,'onerror':PyJs_onError_238_,'onmessage':PyJs_onMessage_239_})
        PyJsHoisted_SocketAdapter_.func_name = 'SocketAdapter'
        var.put('SocketAdapter', PyJsHoisted_SocketAdapter_)
        Js('use strict')
        var.put('decompressPng', var.get('require')(Js('../util/decompressPng')))
        var.put('CBOR', var.get('require')(Js('cbor-js')))
        var.put('typedArrayTagger', var.get('require')(Js('../util/cborTypedArrayTags')))
        var.put('BSON', var.get(u"null"))
        if PyJsStrictNeq(var.get('bson',throw=False).typeof(),Js('undefined')):
            var.put('BSON', var.get('bson')().get('BSON'))
        pass
        var.get('module').put('exports', var.get('SocketAdapter'))
    PyJs_anonymous_234_._set_name('anonymous')
    @Js
    def PyJs_anonymous_242_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['EventEmitter2', 'Message', 'require', 'module', 'Topic', 'exports'])
        @Js
        def PyJsHoisted_Topic_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['that', 'options'])
            var.put('options', (var.get('options') or Js({})))
            var.get(u"this").put('ros', var.get('options').get('ros'))
            var.get(u"this").put('name', var.get('options').get('name'))
            var.get(u"this").put('messageType', var.get('options').get('messageType'))
            var.get(u"this").put('isAdvertised', Js(False))
            var.get(u"this").put('compression', (var.get('options').get('compression') or Js('none')))
            var.get(u"this").put('throttle_rate', (var.get('options').get('throttle_rate') or Js(0.0)))
            var.get(u"this").put('latch', (var.get('options').get('latch') or Js(False)))
            var.get(u"this").put('queue_size', (var.get('options').get('queue_size') or Js(100.0)))
            var.get(u"this").put('queue_length', (var.get('options').get('queue_length') or Js(0.0)))
            var.get(u"this").put('reconnect_on_close', (var.get('options').get('reconnect_on_close') if PyJsStrictNeq(var.get('options').get('reconnect_on_close'),var.get('undefined')) else Js(True)))
            if ((((var.get(u"this").get('compression') and PyJsStrictNeq(var.get(u"this").get('compression'),Js('png'))) and PyJsStrictNeq(var.get(u"this").get('compression'),Js('cbor'))) and PyJsStrictNeq(var.get(u"this").get('compression'),Js('cbor-raw'))) and PyJsStrictNeq(var.get(u"this").get('compression'),Js('none'))):
                var.get(u"this").callprop('emit', Js('warning'), (var.get(u"this").get('compression')+Js(' compression is not supported. No compression will be used.')))
                var.get(u"this").put('compression', Js('none'))
            if (var.get(u"this").get('throttle_rate')<Js(0.0)):
                var.get(u"this").callprop('emit', Js('warning'), (var.get(u"this").get('throttle_rate')+Js(' is not allowed. Set to 0')))
                var.get(u"this").put('throttle_rate', Js(0.0))
            var.put('that', var.get(u"this"))
            if var.get(u"this").get('reconnect_on_close'):
                @Js
                def PyJs_anonymous_243_(message, this, arguments, var=var):
                    var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
                    var.registers(['message'])
                    var.get('that').get('ros').callprop('callOnConnection', var.get('message'))
                    var.get('that').put('waitForReconnect', Js(False))
                    @Js
                    def PyJs_anonymous_244_(this, arguments, var=var):
                        var = Scope({'this':this, 'arguments':arguments}, var)
                        var.registers([])
                        if var.get('that').get('waitForReconnect').neg():
                            var.get('that').put('waitForReconnect', Js(True))
                            var.get('that').get('ros').callprop('callOnConnection', var.get('message'))
                            @Js
                            def PyJs_anonymous_245_(this, arguments, var=var):
                                var = Scope({'this':this, 'arguments':arguments}, var)
                                var.registers([])
                                var.get('that').put('waitForReconnect', Js(False))
                            PyJs_anonymous_245_._set_name('anonymous')
                            var.get('that').get('ros').callprop('once', Js('connection'), PyJs_anonymous_245_)
                    PyJs_anonymous_244_._set_name('anonymous')
                    var.get('that').put('reconnectFunc', PyJs_anonymous_244_)
                    var.get('that').get('ros').callprop('on', Js('close'), var.get('that').get('reconnectFunc'))
                PyJs_anonymous_243_._set_name('anonymous')
                var.get(u"this").put('callForSubscribeAndAdvertise', PyJs_anonymous_243_)
            else:
                var.get(u"this").put('callForSubscribeAndAdvertise', var.get(u"this").get('ros').get('callOnConnection'))
            @Js
            def PyJs_anonymous_246_(data, this, arguments, var=var):
                var = Scope({'data':data, 'this':this, 'arguments':arguments}, var)
                var.registers(['data'])
                var.get('that').callprop('emit', Js('message'), var.get('Message').create(var.get('data')))
            PyJs_anonymous_246_._set_name('anonymous')
            var.get(u"this").put('_messageCallback', PyJs_anonymous_246_)
        PyJsHoisted_Topic_.func_name = 'Topic'
        var.put('Topic', PyJsHoisted_Topic_)
        var.put('EventEmitter2', var.get('require')(Js('eventemitter2')).get('EventEmitter2'))
        var.put('Message', var.get('require')(Js('./Message')))
        pass
        var.get('Topic').get('prototype').put('__proto__', var.get('EventEmitter2').get('prototype'))
        @Js
        def PyJs_anonymous_247_(callback, this, arguments, var=var):
            var = Scope({'callback':callback, 'this':this, 'arguments':arguments}, var)
            var.registers(['callback'])
            if PyJsStrictEq(var.get('callback',throw=False).typeof(),Js('function')):
                var.get(u"this").callprop('on', Js('message'), var.get('callback'))
            if var.get(u"this").get('subscribeId'):
                return var.get('undefined')
            var.get(u"this").get('ros').callprop('on', var.get(u"this").get('name'), var.get(u"this").get('_messageCallback'))
            var.get(u"this").put('subscribeId', (((Js('subscribe:')+var.get(u"this").get('name'))+Js(':'))+var.get(u"this").get('ros').put('idCounter',Js(var.get(u"this").get('ros').get('idCounter').to_number())+Js(1))))
            var.get(u"this").callprop('callForSubscribeAndAdvertise', Js({'op':Js('subscribe'),'id':var.get(u"this").get('subscribeId'),'type':var.get(u"this").get('messageType'),'topic':var.get(u"this").get('name'),'compression':var.get(u"this").get('compression'),'throttle_rate':var.get(u"this").get('throttle_rate'),'queue_length':var.get(u"this").get('queue_length')}))
        PyJs_anonymous_247_._set_name('anonymous')
        var.get('Topic').get('prototype').put('subscribe', PyJs_anonymous_247_)
        @Js
        def PyJs_anonymous_248_(callback, this, arguments, var=var):
            var = Scope({'callback':callback, 'this':this, 'arguments':arguments}, var)
            var.registers(['callback'])
            if var.get('callback'):
                var.get(u"this").callprop('off', Js('message'), var.get('callback'))
                if var.get(u"this").callprop('listeners', Js('message')).get('length'):
                    return var.get('undefined')
            if var.get(u"this").get('subscribeId').neg():
                return var.get('undefined')
            var.get(u"this").get('ros').callprop('off', var.get(u"this").get('name'), var.get(u"this").get('_messageCallback'))
            if var.get(u"this").get('reconnect_on_close'):
                var.get(u"this").get('ros').callprop('off', Js('close'), var.get(u"this").get('reconnectFunc'))
            var.get(u"this").callprop('emit', Js('unsubscribe'))
            var.get(u"this").get('ros').callprop('callOnConnection', Js({'op':Js('unsubscribe'),'id':var.get(u"this").get('subscribeId'),'topic':var.get(u"this").get('name')}))
            var.get(u"this").put('subscribeId', var.get(u"null"))
        PyJs_anonymous_248_._set_name('anonymous')
        var.get('Topic').get('prototype').put('unsubscribe', PyJs_anonymous_248_)
        @Js
        def PyJs_anonymous_249_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['that'])
            if var.get(u"this").get('isAdvertised'):
                return var.get('undefined')
            var.get(u"this").put('advertiseId', (((Js('advertise:')+var.get(u"this").get('name'))+Js(':'))+var.get(u"this").get('ros').put('idCounter',Js(var.get(u"this").get('ros').get('idCounter').to_number())+Js(1))))
            var.get(u"this").callprop('callForSubscribeAndAdvertise', Js({'op':Js('advertise'),'id':var.get(u"this").get('advertiseId'),'type':var.get(u"this").get('messageType'),'topic':var.get(u"this").get('name'),'latch':var.get(u"this").get('latch'),'queue_size':var.get(u"this").get('queue_size')}))
            var.get(u"this").put('isAdvertised', Js(True))
            if var.get(u"this").get('reconnect_on_close').neg():
                var.put('that', var.get(u"this"))
                @Js
                def PyJs_anonymous_250_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    var.get('that').put('isAdvertised', Js(False))
                PyJs_anonymous_250_._set_name('anonymous')
                var.get(u"this").get('ros').callprop('on', Js('close'), PyJs_anonymous_250_)
        PyJs_anonymous_249_._set_name('anonymous')
        var.get('Topic').get('prototype').put('advertise', PyJs_anonymous_249_)
        @Js
        def PyJs_anonymous_251_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            if var.get(u"this").get('isAdvertised').neg():
                return var.get('undefined')
            if var.get(u"this").get('reconnect_on_close'):
                var.get(u"this").get('ros').callprop('off', Js('close'), var.get(u"this").get('reconnectFunc'))
            var.get(u"this").callprop('emit', Js('unadvertise'))
            var.get(u"this").get('ros').callprop('callOnConnection', Js({'op':Js('unadvertise'),'id':var.get(u"this").get('advertiseId'),'topic':var.get(u"this").get('name')}))
            var.get(u"this").put('isAdvertised', Js(False))
        PyJs_anonymous_251_._set_name('anonymous')
        var.get('Topic').get('prototype').put('unadvertise', PyJs_anonymous_251_)
        @Js
        def PyJs_anonymous_252_(message, this, arguments, var=var):
            var = Scope({'message':message, 'this':this, 'arguments':arguments}, var)
            var.registers(['call', 'message'])
            if var.get(u"this").get('isAdvertised').neg():
                var.get(u"this").callprop('advertise')
            (var.get(u"this").get('ros').put('idCounter',Js(var.get(u"this").get('ros').get('idCounter').to_number())+Js(1))-Js(1))
            var.put('call', Js({'op':Js('publish'),'id':(((Js('publish:')+var.get(u"this").get('name'))+Js(':'))+var.get(u"this").get('ros').get('idCounter')),'topic':var.get(u"this").get('name'),'msg':var.get('message'),'latch':var.get(u"this").get('latch')}))
            var.get(u"this").get('ros').callprop('callOnConnection', var.get('call'))
        PyJs_anonymous_252_._set_name('anonymous')
        var.get('Topic').get('prototype').put('publish', PyJs_anonymous_252_)
        var.get('module').put('exports', var.get('Topic'))
    PyJs_anonymous_242_._set_name('anonymous')
    @Js
    def PyJs_anonymous_253_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['mixin', 'require', 'module', 'exports', 'core'])
        var.put('mixin', var.get('require')(Js('../mixin')))
        var.put('core', var.get('module').put('exports', Js({'Ros':var.get('require')(Js('./Ros')),'Topic':var.get('require')(Js('./Topic')),'Message':var.get('require')(Js('./Message')),'Param':var.get('require')(Js('./Param')),'Service':var.get('require')(Js('./Service')),'ServiceRequest':var.get('require')(Js('./ServiceRequest')),'ServiceResponse':var.get('require')(Js('./ServiceResponse'))})))
        var.get('mixin')(var.get('core').get('Ros'), Js([Js('Param'), Js('Service'), Js('Topic')]), var.get('core'))
    PyJs_anonymous_253_._set_name('anonymous')
    @Js
    def PyJs_anonymous_254_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['require', 'Vector3', 'Pose', 'module', 'Quaternion', 'exports'])
        @Js
        def PyJsHoisted_Pose_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['options'])
            var.put('options', (var.get('options') or Js({})))
            var.get(u"this").put('position', var.get('Vector3').create(var.get('options').get('position')))
            var.get(u"this").put('orientation', var.get('Quaternion').create(var.get('options').get('orientation')))
        PyJsHoisted_Pose_.func_name = 'Pose'
        var.put('Pose', PyJsHoisted_Pose_)
        var.put('Vector3', var.get('require')(Js('./Vector3')))
        var.put('Quaternion', var.get('require')(Js('./Quaternion')))
        pass
        @Js
        def PyJs_anonymous_255_(tf, this, arguments, var=var):
            var = Scope({'tf':tf, 'this':this, 'arguments':arguments}, var)
            var.registers(['tf', 'tmp'])
            var.get(u"this").get('position').callprop('multiplyQuaternion', var.get('tf').get('rotation'))
            var.get(u"this").get('position').callprop('add', var.get('tf').get('translation'))
            var.put('tmp', var.get('tf').get('rotation').callprop('clone'))
            var.get('tmp').callprop('multiply', var.get(u"this").get('orientation'))
            var.get(u"this").put('orientation', var.get('tmp'))
        PyJs_anonymous_255_._set_name('anonymous')
        var.get('Pose').get('prototype').put('applyTransform', PyJs_anonymous_255_)
        @Js
        def PyJs_anonymous_256_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get('Pose').create(var.get(u"this"))
        PyJs_anonymous_256_._set_name('anonymous')
        var.get('Pose').get('prototype').put('clone', PyJs_anonymous_256_)
        @Js
        def PyJs_anonymous_257_(pose, this, arguments, var=var):
            var = Scope({'pose':pose, 'this':this, 'arguments':arguments}, var)
            var.registers(['pose', 'p'])
            var.put('p', var.get('pose').callprop('clone'))
            var.get('p').callprop('applyTransform', Js({'rotation':var.get(u"this").get('orientation'),'translation':var.get(u"this").get('position')}))
            return var.get('p')
        PyJs_anonymous_257_._set_name('anonymous')
        var.get('Pose').get('prototype').put('multiply', PyJs_anonymous_257_)
        @Js
        def PyJs_anonymous_258_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['inverse'])
            var.put('inverse', var.get(u"this").callprop('clone'))
            var.get('inverse').get('orientation').callprop('invert')
            var.get('inverse').get('position').callprop('multiplyQuaternion', var.get('inverse').get('orientation'))
            var.get('inverse').get('position').put('x', (-Js(1.0)), '*')
            var.get('inverse').get('position').put('y', (-Js(1.0)), '*')
            var.get('inverse').get('position').put('z', (-Js(1.0)), '*')
            return var.get('inverse')
        PyJs_anonymous_258_._set_name('anonymous')
        var.get('Pose').get('prototype').put('getInverse', PyJs_anonymous_258_)
        var.get('module').put('exports', var.get('Pose'))
    PyJs_anonymous_254_._set_name('anonymous')
    @Js
    def PyJs_anonymous_259_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['Quaternion', 'module', 'require', 'exports'])
        @Js
        def PyJsHoisted_Quaternion_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['options'])
            var.put('options', (var.get('options') or Js({})))
            var.get(u"this").put('x', (var.get('options').get('x') or Js(0.0)))
            var.get(u"this").put('y', (var.get('options').get('y') or Js(0.0)))
            var.get(u"this").put('z', (var.get('options').get('z') or Js(0.0)))
            var.get(u"this").put('w', (var.get('options').get('w') if PyJsStrictEq(var.get('options').get('w').typeof(),Js('number')) else Js(1.0)))
        PyJsHoisted_Quaternion_.func_name = 'Quaternion'
        var.put('Quaternion', PyJsHoisted_Quaternion_)
        pass
        @Js
        def PyJs_anonymous_260_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            var.get(u"this").put('x', (-Js(1.0)), '*')
            var.get(u"this").put('y', (-Js(1.0)), '*')
            var.get(u"this").put('z', (-Js(1.0)), '*')
        PyJs_anonymous_260_._set_name('anonymous')
        var.get('Quaternion').get('prototype').put('conjugate', PyJs_anonymous_260_)
        @Js
        def PyJs_anonymous_261_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get('Math').callprop('sqrt', ((((var.get(u"this").get('x')*var.get(u"this").get('x'))+(var.get(u"this").get('y')*var.get(u"this").get('y')))+(var.get(u"this").get('z')*var.get(u"this").get('z')))+(var.get(u"this").get('w')*var.get(u"this").get('w'))))
        PyJs_anonymous_261_._set_name('anonymous')
        var.get('Quaternion').get('prototype').put('norm', PyJs_anonymous_261_)
        @Js
        def PyJs_anonymous_262_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['l'])
            var.put('l', var.get('Math').callprop('sqrt', ((((var.get(u"this").get('x')*var.get(u"this").get('x'))+(var.get(u"this").get('y')*var.get(u"this").get('y')))+(var.get(u"this").get('z')*var.get(u"this").get('z')))+(var.get(u"this").get('w')*var.get(u"this").get('w')))))
            if PyJsStrictEq(var.get('l'),Js(0.0)):
                var.get(u"this").put('x', Js(0.0))
                var.get(u"this").put('y', Js(0.0))
                var.get(u"this").put('z', Js(0.0))
                var.get(u"this").put('w', Js(1.0))
            else:
                var.put('l', (Js(1.0)/var.get('l')))
                var.get(u"this").put('x', (var.get(u"this").get('x')*var.get('l')))
                var.get(u"this").put('y', (var.get(u"this").get('y')*var.get('l')))
                var.get(u"this").put('z', (var.get(u"this").get('z')*var.get('l')))
                var.get(u"this").put('w', (var.get(u"this").get('w')*var.get('l')))
        PyJs_anonymous_262_._set_name('anonymous')
        var.get('Quaternion').get('prototype').put('normalize', PyJs_anonymous_262_)
        @Js
        def PyJs_anonymous_263_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            var.get(u"this").callprop('conjugate')
            var.get(u"this").callprop('normalize')
        PyJs_anonymous_263_._set_name('anonymous')
        var.get('Quaternion').get('prototype').put('invert', PyJs_anonymous_263_)
        @Js
        def PyJs_anonymous_264_(q, this, arguments, var=var):
            var = Scope({'q':q, 'this':this, 'arguments':arguments}, var)
            var.registers(['q', 'newW', 'newX', 'newZ', 'newY'])
            var.put('newX', ((((var.get(u"this").get('x')*var.get('q').get('w'))+(var.get(u"this").get('y')*var.get('q').get('z')))-(var.get(u"this").get('z')*var.get('q').get('y')))+(var.get(u"this").get('w')*var.get('q').get('x'))))
            var.put('newY', (((((-var.get(u"this").get('x'))*var.get('q').get('z'))+(var.get(u"this").get('y')*var.get('q').get('w')))+(var.get(u"this").get('z')*var.get('q').get('x')))+(var.get(u"this").get('w')*var.get('q').get('y'))))
            var.put('newZ', ((((var.get(u"this").get('x')*var.get('q').get('y'))-(var.get(u"this").get('y')*var.get('q').get('x')))+(var.get(u"this").get('z')*var.get('q').get('w')))+(var.get(u"this").get('w')*var.get('q').get('z'))))
            var.put('newW', (((((-var.get(u"this").get('x'))*var.get('q').get('x'))-(var.get(u"this").get('y')*var.get('q').get('y')))-(var.get(u"this").get('z')*var.get('q').get('z')))+(var.get(u"this").get('w')*var.get('q').get('w'))))
            var.get(u"this").put('x', var.get('newX'))
            var.get(u"this").put('y', var.get('newY'))
            var.get(u"this").put('z', var.get('newZ'))
            var.get(u"this").put('w', var.get('newW'))
        PyJs_anonymous_264_._set_name('anonymous')
        var.get('Quaternion').get('prototype').put('multiply', PyJs_anonymous_264_)
        @Js
        def PyJs_anonymous_265_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get('Quaternion').create(var.get(u"this"))
        PyJs_anonymous_265_._set_name('anonymous')
        var.get('Quaternion').get('prototype').put('clone', PyJs_anonymous_265_)
        var.get('module').put('exports', var.get('Quaternion'))
    PyJs_anonymous_259_._set_name('anonymous')
    @Js
    def PyJs_anonymous_266_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['Transform', 'require', 'Vector3', 'module', 'Quaternion', 'exports'])
        @Js
        def PyJsHoisted_Transform_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['options'])
            var.put('options', (var.get('options') or Js({})))
            var.get(u"this").put('translation', var.get('Vector3').create(var.get('options').get('translation')))
            var.get(u"this").put('rotation', var.get('Quaternion').create(var.get('options').get('rotation')))
        PyJsHoisted_Transform_.func_name = 'Transform'
        var.put('Transform', PyJsHoisted_Transform_)
        var.put('Vector3', var.get('require')(Js('./Vector3')))
        var.put('Quaternion', var.get('require')(Js('./Quaternion')))
        pass
        @Js
        def PyJs_anonymous_267_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get('Transform').create(var.get(u"this"))
        PyJs_anonymous_267_._set_name('anonymous')
        var.get('Transform').get('prototype').put('clone', PyJs_anonymous_267_)
        var.get('module').put('exports', var.get('Transform'))
    PyJs_anonymous_266_._set_name('anonymous')
    @Js
    def PyJs_anonymous_268_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['exports', 'module', 'require', 'Vector3'])
        @Js
        def PyJsHoisted_Vector3_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['options'])
            var.put('options', (var.get('options') or Js({})))
            var.get(u"this").put('x', (var.get('options').get('x') or Js(0.0)))
            var.get(u"this").put('y', (var.get('options').get('y') or Js(0.0)))
            var.get(u"this").put('z', (var.get('options').get('z') or Js(0.0)))
        PyJsHoisted_Vector3_.func_name = 'Vector3'
        var.put('Vector3', PyJsHoisted_Vector3_)
        pass
        @Js
        def PyJs_anonymous_269_(v, this, arguments, var=var):
            var = Scope({'v':v, 'this':this, 'arguments':arguments}, var)
            var.registers(['v'])
            var.get(u"this").put('x', var.get('v').get('x'), '+')
            var.get(u"this").put('y', var.get('v').get('y'), '+')
            var.get(u"this").put('z', var.get('v').get('z'), '+')
        PyJs_anonymous_269_._set_name('anonymous')
        var.get('Vector3').get('prototype').put('add', PyJs_anonymous_269_)
        @Js
        def PyJs_anonymous_270_(v, this, arguments, var=var):
            var = Scope({'v':v, 'this':this, 'arguments':arguments}, var)
            var.registers(['v'])
            var.get(u"this").put('x', var.get('v').get('x'), '-')
            var.get(u"this").put('y', var.get('v').get('y'), '-')
            var.get(u"this").put('z', var.get('v').get('z'), '-')
        PyJs_anonymous_270_._set_name('anonymous')
        var.get('Vector3').get('prototype').put('subtract', PyJs_anonymous_270_)
        @Js
        def PyJs_anonymous_271_(q, this, arguments, var=var):
            var = Scope({'q':q, 'this':this, 'arguments':arguments}, var)
            var.registers(['iy', 'q', 'iw', 'ix', 'iz'])
            var.put('ix', (((var.get('q').get('w')*var.get(u"this").get('x'))+(var.get('q').get('y')*var.get(u"this").get('z')))-(var.get('q').get('z')*var.get(u"this").get('y'))))
            var.put('iy', (((var.get('q').get('w')*var.get(u"this").get('y'))+(var.get('q').get('z')*var.get(u"this").get('x')))-(var.get('q').get('x')*var.get(u"this").get('z'))))
            var.put('iz', (((var.get('q').get('w')*var.get(u"this").get('z'))+(var.get('q').get('x')*var.get(u"this").get('y')))-(var.get('q').get('y')*var.get(u"this").get('x'))))
            var.put('iw', ((((-var.get('q').get('x'))*var.get(u"this").get('x'))-(var.get('q').get('y')*var.get(u"this").get('y')))-(var.get('q').get('z')*var.get(u"this").get('z'))))
            var.get(u"this").put('x', ((((var.get('ix')*var.get('q').get('w'))+(var.get('iw')*(-var.get('q').get('x'))))+(var.get('iy')*(-var.get('q').get('z'))))-(var.get('iz')*(-var.get('q').get('y')))))
            var.get(u"this").put('y', ((((var.get('iy')*var.get('q').get('w'))+(var.get('iw')*(-var.get('q').get('y'))))+(var.get('iz')*(-var.get('q').get('x'))))-(var.get('ix')*(-var.get('q').get('z')))))
            var.get(u"this").put('z', ((((var.get('iz')*var.get('q').get('w'))+(var.get('iw')*(-var.get('q').get('z'))))+(var.get('ix')*(-var.get('q').get('y'))))-(var.get('iy')*(-var.get('q').get('x')))))
        PyJs_anonymous_271_._set_name('anonymous')
        var.get('Vector3').get('prototype').put('multiplyQuaternion', PyJs_anonymous_271_)
        @Js
        def PyJs_anonymous_272_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get('Vector3').create(var.get(u"this"))
        PyJs_anonymous_272_._set_name('anonymous')
        var.get('Vector3').get('prototype').put('clone', PyJs_anonymous_272_)
        var.get('module').put('exports', var.get('Vector3'))
    PyJs_anonymous_268_._set_name('anonymous')
    @Js
    def PyJs_anonymous_273_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['module', 'require', 'exports'])
        var.get('module').put('exports', Js({'Pose':var.get('require')(Js('./Pose')),'Quaternion':var.get('require')(Js('./Quaternion')),'Transform':var.get('require')(Js('./Transform')),'Vector3':var.get('require')(Js('./Vector3'))}))
    PyJs_anonymous_273_._set_name('anonymous')
    @Js
    def PyJs_anonymous_274_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['module', 'require', 'exports'])
        @Js
        def PyJs_anonymous_275_(Ros, classes, features, this, arguments, var=var):
            var = Scope({'Ros':Ros, 'classes':classes, 'features':features, 'this':this, 'arguments':arguments}, var)
            var.registers(['features', 'Ros', 'classes'])
            @Js
            def PyJs_anonymous_276_(className, this, arguments, var=var):
                var = Scope({'className':className, 'this':this, 'arguments':arguments}, var)
                var.registers(['Class', 'className'])
                var.put('Class', var.get('features').get(var.get('className')))
                @Js
                def PyJs_anonymous_277_(options, this, arguments, var=var):
                    var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
                    var.registers(['options'])
                    var.get('options').put('ros', var.get(u"this"))
                    return var.get('Class').create(var.get('options'))
                PyJs_anonymous_277_._set_name('anonymous')
                var.get('Ros').get('prototype').put(var.get('className'), PyJs_anonymous_277_)
            PyJs_anonymous_276_._set_name('anonymous')
            var.get('classes').callprop('forEach', PyJs_anonymous_276_)
        PyJs_anonymous_275_._set_name('anonymous')
        var.get('module').put('exports', PyJs_anonymous_275_)
    PyJs_anonymous_274_._set_name('anonymous')
    @Js
    def PyJs_anonymous_278_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['Transform', 'ActionClient', 'require', 'Topic', 'module', 'Goal', 'Service', 'ServiceRequest', 'exports', 'TFClient'])
        @Js
        def PyJsHoisted_TFClient_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['nsecs', 'secs', 'seconds', 'options'])
            var.put('options', (var.get('options') or Js({})))
            var.get(u"this").put('ros', var.get('options').get('ros'))
            var.get(u"this").put('fixedFrame', (var.get('options').get('fixedFrame') or Js('/base_link')))
            var.get(u"this").put('angularThres', (var.get('options').get('angularThres') or Js(2.0)))
            var.get(u"this").put('transThres', (var.get('options').get('transThres') or Js(0.01)))
            var.get(u"this").put('rate', (var.get('options').get('rate') or Js(10.0)))
            var.get(u"this").put('updateDelay', (var.get('options').get('updateDelay') or Js(50.0)))
            var.put('seconds', (var.get('options').get('topicTimeout') or Js(2.0)))
            var.put('secs', var.get('Math').callprop('floor', var.get('seconds')))
            var.put('nsecs', var.get('Math').callprop('floor', ((var.get('seconds')-var.get('secs'))*Js(1000000000.0))))
            var.get(u"this").put('topicTimeout', Js({'secs':var.get('secs'),'nsecs':var.get('nsecs')}))
            var.get(u"this").put('serverName', (var.get('options').get('serverName') or Js('/tf2_web_republisher')))
            var.get(u"this").put('repubServiceName', (var.get('options').get('repubServiceName') or Js('/republish_tfs')))
            var.get(u"this").put('currentGoal', Js(False))
            var.get(u"this").put('currentTopic', Js(False))
            var.get(u"this").put('frameInfos', Js({}))
            var.get(u"this").put('republisherUpdateRequested', Js(False))
            var.get(u"this").put('_subscribeCB', var.get(u"null"))
            var.get(u"this").put('_isDisposed', Js(False))
            var.get(u"this").put('actionClient', var.get('ActionClient').create(Js({'ros':var.get('options').get('ros'),'serverName':var.get(u"this").get('serverName'),'actionName':Js('tf2_web_republisher/TFSubscriptionAction'),'omitStatus':Js(True),'omitResult':Js(True)})))
            var.get(u"this").put('serviceClient', var.get('Service').create(Js({'ros':var.get('options').get('ros'),'name':var.get(u"this").get('repubServiceName'),'serviceType':Js('tf2_web_republisher/RepublishTFs')})))
        PyJsHoisted_TFClient_.func_name = 'TFClient'
        var.put('TFClient', PyJsHoisted_TFClient_)
        var.put('ActionClient', var.get('require')(Js('../actionlib/ActionClient')))
        var.put('Goal', var.get('require')(Js('../actionlib/Goal')))
        var.put('Service', var.get('require')(Js('../core/Service.js')))
        var.put('ServiceRequest', var.get('require')(Js('../core/ServiceRequest.js')))
        var.put('Topic', var.get('require')(Js('../core/Topic.js')))
        var.put('Transform', var.get('require')(Js('../math/Transform')))
        pass
        @Js
        def PyJs_anonymous_279_(tf, this, arguments, var=var):
            var = Scope({'tf':tf, 'this':this, 'arguments':arguments}, var)
            var.registers(['that', 'tf'])
            var.put('that', var.get(u"this"))
            @Js
            def PyJs_anonymous_280_(transform, this, arguments, var=var):
                var = Scope({'transform':transform, 'this':this, 'arguments':arguments}, var)
                var.registers(['frameID', 'info', 'transform'])
                var.put('frameID', var.get('transform').get('child_frame_id'))
                if PyJsStrictEq(var.get('frameID').get('0'),Js('/')):
                    var.put('frameID', var.get('frameID').callprop('substring', Js(1.0)))
                var.put('info', var.get(u"this").get('frameInfos').get(var.get('frameID')))
                if var.get('info'):
                    var.get('info').put('transform', var.get('Transform').create(Js({'translation':var.get('transform').get('transform').get('translation'),'rotation':var.get('transform').get('transform').get('rotation')})))
                    @Js
                    def PyJs_anonymous_281_(cb, this, arguments, var=var):
                        var = Scope({'cb':cb, 'this':this, 'arguments':arguments}, var)
                        var.registers(['cb'])
                        var.get('cb')(var.get('info').get('transform'))
                    PyJs_anonymous_281_._set_name('anonymous')
                    var.get('info').get('cbs').callprop('forEach', PyJs_anonymous_281_)
            PyJs_anonymous_280_._set_name('anonymous')
            var.get('tf').get('transforms').callprop('forEach', PyJs_anonymous_280_, var.get(u"this"))
        PyJs_anonymous_279_._set_name('anonymous')
        var.get('TFClient').get('prototype').put('processTFArray', PyJs_anonymous_279_)
        @Js
        def PyJs_anonymous_282_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['goalMessage', 'request'])
            var.put('goalMessage', Js({'source_frames':var.get('Object').callprop('keys', var.get(u"this").get('frameInfos')),'target_frame':var.get(u"this").get('fixedFrame'),'angular_thres':var.get(u"this").get('angularThres'),'trans_thres':var.get(u"this").get('transThres'),'rate':var.get(u"this").get('rate')}))
            if var.get(u"this").get('ros').get('groovyCompatibility'):
                if var.get(u"this").get('currentGoal'):
                    var.get(u"this").get('currentGoal').callprop('cancel')
                var.get(u"this").put('currentGoal', var.get('Goal').create(Js({'actionClient':var.get(u"this").get('actionClient'),'goalMessage':var.get('goalMessage')})))
                var.get(u"this").get('currentGoal').callprop('on', Js('feedback'), var.get(u"this").get('processTFArray').callprop('bind', var.get(u"this")))
                var.get(u"this").get('currentGoal').callprop('send')
            else:
                var.get('goalMessage').put('timeout', var.get(u"this").get('topicTimeout'))
                var.put('request', var.get('ServiceRequest').create(var.get('goalMessage')))
                var.get(u"this").get('serviceClient').callprop('callService', var.get('request'), var.get(u"this").get('processResponse').callprop('bind', var.get(u"this")))
            var.get(u"this").put('republisherUpdateRequested', Js(False))
        PyJs_anonymous_282_._set_name('anonymous')
        var.get('TFClient').get('prototype').put('updateGoal', PyJs_anonymous_282_)
        @Js
        def PyJs_anonymous_283_(response, this, arguments, var=var):
            var = Scope({'response':response, 'this':this, 'arguments':arguments}, var)
            var.registers(['response'])
            if var.get(u"this").get('_isDisposed'):
                return var.get('undefined')
            if var.get(u"this").get('currentTopic'):
                var.get(u"this").get('currentTopic').callprop('unsubscribe', var.get(u"this").get('_subscribeCB'))
            var.get(u"this").put('currentTopic', var.get('Topic').create(Js({'ros':var.get(u"this").get('ros'),'name':var.get('response').get('topic_name'),'messageType':Js('tf2_web_republisher/TFArray')})))
            var.get(u"this").put('_subscribeCB', var.get(u"this").get('processTFArray').callprop('bind', var.get(u"this")))
            var.get(u"this").get('currentTopic').callprop('subscribe', var.get(u"this").get('_subscribeCB'))
        PyJs_anonymous_283_._set_name('anonymous')
        var.get('TFClient').get('prototype').put('processResponse', PyJs_anonymous_283_)
        @Js
        def PyJs_anonymous_284_(frameID, callback, this, arguments, var=var):
            var = Scope({'frameID':frameID, 'callback':callback, 'this':this, 'arguments':arguments}, var)
            var.registers(['frameID', 'callback'])
            if PyJsStrictEq(var.get('frameID').get('0'),Js('/')):
                var.put('frameID', var.get('frameID').callprop('substring', Js(1.0)))
            if var.get(u"this").get('frameInfos').get(var.get('frameID')).neg():
                var.get(u"this").get('frameInfos').put(var.get('frameID'), Js({'cbs':Js([])}))
                if var.get(u"this").get('republisherUpdateRequested').neg():
                    var.get('setTimeout')(var.get(u"this").get('updateGoal').callprop('bind', var.get(u"this")), var.get(u"this").get('updateDelay'))
                    var.get(u"this").put('republisherUpdateRequested', Js(True))
            else:
                if var.get(u"this").get('frameInfos').get(var.get('frameID')).get('transform'):
                    var.get('callback')(var.get(u"this").get('frameInfos').get(var.get('frameID')).get('transform'))
            var.get(u"this").get('frameInfos').get(var.get('frameID')).get('cbs').callprop('push', var.get('callback'))
        PyJs_anonymous_284_._set_name('anonymous')
        var.get('TFClient').get('prototype').put('subscribe', PyJs_anonymous_284_)
        @Js
        def PyJs_anonymous_285_(frameID, callback, this, arguments, var=var):
            var = Scope({'frameID':frameID, 'callback':callback, 'this':this, 'arguments':arguments}, var)
            var.registers(['frameID', 'callback', 'idx', 'info', 'cbs'])
            if PyJsStrictEq(var.get('frameID').get('0'),Js('/')):
                var.put('frameID', var.get('frameID').callprop('substring', Js(1.0)))
            var.put('info', var.get(u"this").get('frameInfos').get(var.get('frameID')))
            #for JS loop
            var.put('cbs', ((var.get('info') and var.get('info').get('cbs')) or Js([])))
            var.put('idx', var.get('cbs').get('length'))
            while (var.put('idx',Js(var.get('idx').to_number())-Js(1))+Js(1)):
                if PyJsStrictEq(var.get('cbs').get(var.get('idx')),var.get('callback')):
                    var.get('cbs').callprop('splice', var.get('idx'), Js(1.0))
            
            if (var.get('callback').neg() or PyJsStrictEq(var.get('cbs').get('length'),Js(0.0))):
                var.get(u"this").get('frameInfos').delete(var.get('frameID'))
        PyJs_anonymous_285_._set_name('anonymous')
        var.get('TFClient').get('prototype').put('unsubscribe', PyJs_anonymous_285_)
        @Js
        def PyJs_anonymous_286_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            var.get(u"this").put('_isDisposed', Js(True))
            var.get(u"this").get('actionClient').callprop('dispose')
            if var.get(u"this").get('currentTopic'):
                var.get(u"this").get('currentTopic').callprop('unsubscribe', var.get(u"this").get('_subscribeCB'))
        PyJs_anonymous_286_._set_name('anonymous')
        var.get('TFClient').get('prototype').put('dispose', PyJs_anonymous_286_)
        var.get('module').put('exports', var.get('TFClient'))
    PyJs_anonymous_278_._set_name('anonymous')
    @Js
    def PyJs_anonymous_287_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['mixin', 'tf', 'require', 'Ros', 'module', 'exports'])
        var.put('Ros', var.get('require')(Js('../core/Ros')))
        var.put('mixin', var.get('require')(Js('../mixin')))
        var.put('tf', var.get('module').put('exports', Js({'TFClient':var.get('require')(Js('./TFClient'))})))
        var.get('mixin')(var.get('Ros'), Js([Js('TFClient')]), var.get('tf'))
    PyJs_anonymous_287_._set_name('anonymous')
    @Js
    def PyJs_anonymous_288_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['require', 'Vector3', 'module', 'UrdfTypes', 'UrdfBox', 'exports'])
        @Js
        def PyJsHoisted_UrdfBox_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['xyz', 'options'])
            var.get(u"this").put('dimension', var.get(u"null"))
            var.get(u"this").put('type', var.get('UrdfTypes').get('URDF_BOX'))
            var.put('xyz', var.get('options').get('xml').callprop('getAttribute', Js('size')).callprop('split', Js(' ')))
            var.get(u"this").put('dimension', var.get('Vector3').create(Js({'x':var.get('parseFloat')(var.get('xyz').get('0')),'y':var.get('parseFloat')(var.get('xyz').get('1')),'z':var.get('parseFloat')(var.get('xyz').get('2'))})))
        PyJsHoisted_UrdfBox_.func_name = 'UrdfBox'
        var.put('UrdfBox', PyJsHoisted_UrdfBox_)
        var.put('Vector3', var.get('require')(Js('../math/Vector3')))
        var.put('UrdfTypes', var.get('require')(Js('./UrdfTypes')))
        pass
        var.get('module').put('exports', var.get('UrdfBox'))
    PyJs_anonymous_288_._set_name('anonymous')
    @Js
    def PyJs_anonymous_289_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['module', 'require', 'UrdfColor', 'exports'])
        @Js
        def PyJsHoisted_UrdfColor_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['rgba', 'options'])
            var.put('rgba', var.get('options').get('xml').callprop('getAttribute', Js('rgba')).callprop('split', Js(' ')))
            var.get(u"this").put('r', var.get('parseFloat')(var.get('rgba').get('0')))
            var.get(u"this").put('g', var.get('parseFloat')(var.get('rgba').get('1')))
            var.get(u"this").put('b', var.get('parseFloat')(var.get('rgba').get('2')))
            var.get(u"this").put('a', var.get('parseFloat')(var.get('rgba').get('3')))
        PyJsHoisted_UrdfColor_.func_name = 'UrdfColor'
        var.put('UrdfColor', PyJsHoisted_UrdfColor_)
        pass
        var.get('module').put('exports', var.get('UrdfColor'))
    PyJs_anonymous_289_._set_name('anonymous')
    @Js
    def PyJs_anonymous_290_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['require', 'module', 'UrdfTypes', 'UrdfCylinder', 'exports'])
        @Js
        def PyJsHoisted_UrdfCylinder_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['options'])
            var.get(u"this").put('type', var.get('UrdfTypes').get('URDF_CYLINDER'))
            var.get(u"this").put('length', var.get('parseFloat')(var.get('options').get('xml').callprop('getAttribute', Js('length'))))
            var.get(u"this").put('radius', var.get('parseFloat')(var.get('options').get('xml').callprop('getAttribute', Js('radius'))))
        PyJsHoisted_UrdfCylinder_.func_name = 'UrdfCylinder'
        var.put('UrdfCylinder', PyJsHoisted_UrdfCylinder_)
        var.put('UrdfTypes', var.get('require')(Js('./UrdfTypes')))
        pass
        var.get('module').put('exports', var.get('UrdfCylinder'))
    PyJs_anonymous_290_._set_name('anonymous')
    @Js
    def PyJs_anonymous_291_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['require', 'Vector3', 'UrdfJoint', 'Pose', 'module', 'Quaternion', 'exports'])
        @Js
        def PyJsHoisted_UrdfJoint_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'rpy', 'pitch', 'origins', 'orientation', 'xyz', 'roll', 'options', 'position', 'w', 'z', 'psi', 'children', 'the', 'phi', 'x', 'parents', 'yaw', 'limits'])
            var.get(u"this").put('name', var.get('options').get('xml').callprop('getAttribute', Js('name')))
            var.get(u"this").put('type', var.get('options').get('xml').callprop('getAttribute', Js('type')))
            var.put('parents', var.get('options').get('xml').callprop('getElementsByTagName', Js('parent')))
            if (var.get('parents').get('length')>Js(0.0)):
                var.get(u"this").put('parent', var.get('parents').get('0').callprop('getAttribute', Js('link')))
            var.put('children', var.get('options').get('xml').callprop('getElementsByTagName', Js('child')))
            if (var.get('children').get('length')>Js(0.0)):
                var.get(u"this").put('child', var.get('children').get('0').callprop('getAttribute', Js('link')))
            var.put('limits', var.get('options').get('xml').callprop('getElementsByTagName', Js('limit')))
            if (var.get('limits').get('length')>Js(0.0)):
                var.get(u"this").put('minval', var.get('parseFloat')(var.get('limits').get('0').callprop('getAttribute', Js('lower'))))
                var.get(u"this").put('maxval', var.get('parseFloat')(var.get('limits').get('0').callprop('getAttribute', Js('upper'))))
            var.put('origins', var.get('options').get('xml').callprop('getElementsByTagName', Js('origin')))
            if PyJsStrictEq(var.get('origins').get('length'),Js(0.0)):
                var.get(u"this").put('origin', var.get('Pose').create())
            else:
                var.put('xyz', var.get('origins').get('0').callprop('getAttribute', Js('xyz')))
                var.put('position', var.get('Vector3').create())
                if var.get('xyz'):
                    var.put('xyz', var.get('xyz').callprop('split', Js(' ')))
                    var.put('position', var.get('Vector3').create(Js({'x':var.get('parseFloat')(var.get('xyz').get('0')),'y':var.get('parseFloat')(var.get('xyz').get('1')),'z':var.get('parseFloat')(var.get('xyz').get('2'))})))
                var.put('rpy', var.get('origins').get('0').callprop('getAttribute', Js('rpy')))
                var.put('orientation', var.get('Quaternion').create())
                if var.get('rpy'):
                    var.put('rpy', var.get('rpy').callprop('split', Js(' ')))
                    var.put('roll', var.get('parseFloat')(var.get('rpy').get('0')))
                    var.put('pitch', var.get('parseFloat')(var.get('rpy').get('1')))
                    var.put('yaw', var.get('parseFloat')(var.get('rpy').get('2')))
                    var.put('phi', (var.get('roll')/Js(2.0)))
                    var.put('the', (var.get('pitch')/Js(2.0)))
                    var.put('psi', (var.get('yaw')/Js(2.0)))
                    var.put('x', (((var.get('Math').callprop('sin', var.get('phi'))*var.get('Math').callprop('cos', var.get('the')))*var.get('Math').callprop('cos', var.get('psi')))-((var.get('Math').callprop('cos', var.get('phi'))*var.get('Math').callprop('sin', var.get('the')))*var.get('Math').callprop('sin', var.get('psi')))))
                    var.put('y', (((var.get('Math').callprop('cos', var.get('phi'))*var.get('Math').callprop('sin', var.get('the')))*var.get('Math').callprop('cos', var.get('psi')))+((var.get('Math').callprop('sin', var.get('phi'))*var.get('Math').callprop('cos', var.get('the')))*var.get('Math').callprop('sin', var.get('psi')))))
                    var.put('z', (((var.get('Math').callprop('cos', var.get('phi'))*var.get('Math').callprop('cos', var.get('the')))*var.get('Math').callprop('sin', var.get('psi')))-((var.get('Math').callprop('sin', var.get('phi'))*var.get('Math').callprop('sin', var.get('the')))*var.get('Math').callprop('cos', var.get('psi')))))
                    var.put('w', (((var.get('Math').callprop('cos', var.get('phi'))*var.get('Math').callprop('cos', var.get('the')))*var.get('Math').callprop('cos', var.get('psi')))+((var.get('Math').callprop('sin', var.get('phi'))*var.get('Math').callprop('sin', var.get('the')))*var.get('Math').callprop('sin', var.get('psi')))))
                    var.put('orientation', var.get('Quaternion').create(Js({'x':var.get('x'),'y':var.get('y'),'z':var.get('z'),'w':var.get('w')})))
                    var.get('orientation').callprop('normalize')
                var.get(u"this").put('origin', var.get('Pose').create(Js({'position':var.get('position'),'orientation':var.get('orientation')})))
        PyJsHoisted_UrdfJoint_.func_name = 'UrdfJoint'
        var.put('UrdfJoint', PyJsHoisted_UrdfJoint_)
        var.put('Pose', var.get('require')(Js('../math/Pose')))
        var.put('Vector3', var.get('require')(Js('../math/Vector3')))
        var.put('Quaternion', var.get('require')(Js('../math/Quaternion')))
        pass
        var.get('module').put('exports', var.get('UrdfJoint'))
    PyJs_anonymous_291_._set_name('anonymous')
    @Js
    def PyJs_anonymous_292_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['require', 'module', 'UrdfVisual', 'UrdfLink', 'exports'])
        @Js
        def PyJsHoisted_UrdfLink_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['visuals', 'i', 'options'])
            var.get(u"this").put('name', var.get('options').get('xml').callprop('getAttribute', Js('name')))
            var.get(u"this").put('visuals', Js([]))
            var.put('visuals', var.get('options').get('xml').callprop('getElementsByTagName', Js('visual')))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('visuals').get('length')):
                try:
                    var.get(u"this").get('visuals').callprop('push', var.get('UrdfVisual').create(Js({'xml':var.get('visuals').get(var.get('i'))})))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        PyJsHoisted_UrdfLink_.func_name = 'UrdfLink'
        var.put('UrdfLink', PyJsHoisted_UrdfLink_)
        var.put('UrdfVisual', var.get('require')(Js('./UrdfVisual')))
        pass
        var.get('module').put('exports', var.get('UrdfLink'))
    PyJs_anonymous_292_._set_name('anonymous')
    @Js
    def PyJs_anonymous_293_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['UrdfMaterial', 'require', 'module', 'assign', 'UrdfColor', 'exports'])
        @Js
        def PyJsHoisted_UrdfMaterial_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['textures', 'colors', 'options'])
            var.get(u"this").put('textureFilename', var.get(u"null"))
            var.get(u"this").put('color', var.get(u"null"))
            var.get(u"this").put('name', var.get('options').get('xml').callprop('getAttribute', Js('name')))
            var.put('textures', var.get('options').get('xml').callprop('getElementsByTagName', Js('texture')))
            if (var.get('textures').get('length')>Js(0.0)):
                var.get(u"this").put('textureFilename', var.get('textures').get('0').callprop('getAttribute', Js('filename')))
            var.put('colors', var.get('options').get('xml').callprop('getElementsByTagName', Js('color')))
            if (var.get('colors').get('length')>Js(0.0)):
                var.get(u"this").put('color', var.get('UrdfColor').create(Js({'xml':var.get('colors').get('0')})))
        PyJsHoisted_UrdfMaterial_.func_name = 'UrdfMaterial'
        var.put('UrdfMaterial', PyJsHoisted_UrdfMaterial_)
        var.put('UrdfColor', var.get('require')(Js('./UrdfColor')))
        pass
        @Js
        def PyJs_anonymous_294_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return (PyJsStrictEq(var.get(u"this").get('color'),var.get(u"null")) and PyJsStrictEq(var.get(u"this").get('textureFilename'),var.get(u"null")))
        PyJs_anonymous_294_._set_name('anonymous')
        var.get('UrdfMaterial').get('prototype').put('isLink', PyJs_anonymous_294_)
        var.put('assign', var.get('require')(Js('object-assign')))
        @Js
        def PyJs_anonymous_295_(obj, this, arguments, var=var):
            var = Scope({'obj':obj, 'this':this, 'arguments':arguments}, var)
            var.registers(['obj'])
            return var.get('assign')(var.get(u"this"), var.get('obj'))
        PyJs_anonymous_295_._set_name('anonymous')
        var.get('UrdfMaterial').get('prototype').put('assign', PyJs_anonymous_295_)
        var.get('module').put('exports', var.get('UrdfMaterial'))
    PyJs_anonymous_293_._set_name('anonymous')
    @Js
    def PyJs_anonymous_296_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['require', 'Vector3', 'UrdfMesh', 'module', 'UrdfTypes', 'exports'])
        @Js
        def PyJsHoisted_UrdfMesh_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['xyz', 'scale', 'options'])
            var.get(u"this").put('scale', var.get(u"null"))
            var.get(u"this").put('type', var.get('UrdfTypes').get('URDF_MESH'))
            var.get(u"this").put('filename', var.get('options').get('xml').callprop('getAttribute', Js('filename')))
            var.put('scale', var.get('options').get('xml').callprop('getAttribute', Js('scale')))
            if var.get('scale'):
                var.put('xyz', var.get('scale').callprop('split', Js(' ')))
                var.get(u"this").put('scale', var.get('Vector3').create(Js({'x':var.get('parseFloat')(var.get('xyz').get('0')),'y':var.get('parseFloat')(var.get('xyz').get('1')),'z':var.get('parseFloat')(var.get('xyz').get('2'))})))
        PyJsHoisted_UrdfMesh_.func_name = 'UrdfMesh'
        var.put('UrdfMesh', PyJsHoisted_UrdfMesh_)
        var.put('Vector3', var.get('require')(Js('../math/Vector3')))
        var.put('UrdfTypes', var.get('require')(Js('./UrdfTypes')))
        pass
        var.get('module').put('exports', var.get('UrdfMesh'))
    PyJs_anonymous_296_._set_name('anonymous')
    @Js
    def PyJs_anonymous_297_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['UrdfMaterial', 'require', 'exports', 'UrdfJoint', 'DOMParser', 'module', 'UrdfModel', 'XPATH_FIRST_ORDERED_NODE_TYPE', 'UrdfLink'])
        @Js
        def PyJsHoisted_UrdfModel_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['node', 'link', 'j', 'i', 'options', 'string', 'robotXml', 'material', 'mat', 'parser', 'joint', 'xmlDoc', 'nodes'])
            var.put('options', (var.get('options') or Js({})))
            var.put('xmlDoc', var.get('options').get('xml'))
            var.put('string', var.get('options').get('string'))
            var.get(u"this").put('materials', Js({}))
            var.get(u"this").put('links', Js({}))
            var.get(u"this").put('joints', Js({}))
            if var.get('string'):
                var.put('parser', var.get('DOMParser').create())
                var.put('xmlDoc', var.get('parser').callprop('parseFromString', var.get('string'), Js('text/xml')))
            var.put('robotXml', var.get('xmlDoc').get('documentElement'))
            var.get(u"this").put('name', var.get('robotXml').callprop('getAttribute', Js('name')))
            #for JS loop
            var.put('nodes', var.get('robotXml').get('childNodes'))
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('nodes').get('length')):
                try:
                    var.put('node', var.get('nodes').get(var.get('i')))
                    if PyJsStrictEq(var.get('node').get('tagName'),Js('material')):
                        var.put('material', var.get('UrdfMaterial').create(Js({'xml':var.get('node')})))
                        if PyJsStrictNeq(var.get(u"this").get('materials').get(var.get('material').get('name')),PyJsComma(Js(0.0), Js(None))):
                            if var.get(u"this").get('materials').get(var.get('material').get('name')).callprop('isLink'):
                                var.get(u"this").get('materials').get(var.get('material').get('name')).callprop('assign', var.get('material'))
                            else:
                                var.get('console').callprop('warn', ((Js('Material ')+var.get('material').get('name'))+Js('is not unique.')))
                        else:
                            var.get(u"this").get('materials').put(var.get('material').get('name'), var.get('material'))
                    else:
                        if PyJsStrictEq(var.get('node').get('tagName'),Js('link')):
                            var.put('link', var.get('UrdfLink').create(Js({'xml':var.get('node')})))
                            if PyJsStrictNeq(var.get(u"this").get('links').get(var.get('link').get('name')),PyJsComma(Js(0.0), Js(None))):
                                var.get('console').callprop('warn', ((Js('Link ')+var.get('link').get('name'))+Js(' is not unique.')))
                            else:
                                #for JS loop
                                var.put('j', Js(0.0))
                                while (var.get('j')<var.get('link').get('visuals').get('length')):
                                    try:
                                        var.put('mat', var.get('link').get('visuals').get(var.get('j')).get('material'))
                                        if (PyJsStrictNeq(var.get('mat'),var.get(u"null")) and var.get('mat').get('name')):
                                            if PyJsStrictNeq(var.get(u"this").get('materials').get(var.get('mat').get('name')),PyJsComma(Js(0.0), Js(None))):
                                                var.get('link').get('visuals').get(var.get('j')).put('material', var.get(u"this").get('materials').get(var.get('mat').get('name')))
                                            else:
                                                var.get(u"this").get('materials').put(var.get('mat').get('name'), var.get('mat'))
                                    finally:
                                            (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                                var.get(u"this").get('links').put(var.get('link').get('name'), var.get('link'))
                        else:
                            if PyJsStrictEq(var.get('node').get('tagName'),Js('joint')):
                                var.put('joint', var.get('UrdfJoint').create(Js({'xml':var.get('node')})))
                                var.get(u"this").get('joints').put(var.get('joint').get('name'), var.get('joint'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        PyJsHoisted_UrdfModel_.func_name = 'UrdfModel'
        var.put('UrdfModel', PyJsHoisted_UrdfModel_)
        var.put('UrdfMaterial', var.get('require')(Js('./UrdfMaterial')))
        var.put('UrdfLink', var.get('require')(Js('./UrdfLink')))
        var.put('UrdfJoint', var.get('require')(Js('./UrdfJoint')))
        var.put('DOMParser', var.get('require')(Js('@xmldom/xmldom')).get('DOMParser'))
        var.put('XPATH_FIRST_ORDERED_NODE_TYPE', Js(9.0))
        pass
        var.get('module').put('exports', var.get('UrdfModel'))
    PyJs_anonymous_297_._set_name('anonymous')
    @Js
    def PyJs_anonymous_298_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['UrdfSphere', 'require', 'module', 'UrdfTypes', 'exports'])
        @Js
        def PyJsHoisted_UrdfSphere_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['options'])
            var.get(u"this").put('type', var.get('UrdfTypes').get('URDF_SPHERE'))
            var.get(u"this").put('radius', var.get('parseFloat')(var.get('options').get('xml').callprop('getAttribute', Js('radius'))))
        PyJsHoisted_UrdfSphere_.func_name = 'UrdfSphere'
        var.put('UrdfSphere', PyJsHoisted_UrdfSphere_)
        var.put('UrdfTypes', var.get('require')(Js('./UrdfTypes')))
        pass
        var.get('module').put('exports', var.get('UrdfSphere'))
    PyJs_anonymous_298_._set_name('anonymous')
    @Js
    def PyJs_anonymous_299_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['module', 'require', 'exports'])
        var.get('module').put('exports', Js({'URDF_SPHERE':Js(0.0),'URDF_BOX':Js(1.0),'URDF_CYLINDER':Js(2.0),'URDF_MESH':Js(3.0)}))
    PyJs_anonymous_299_._set_name('anonymous')
    @Js
    def PyJs_anonymous_300_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['UrdfMaterial', 'UrdfSphere', 'require', 'Vector3', 'Pose', 'UrdfMesh', 'module', 'UrdfBox', 'UrdfVisual', 'Quaternion', 'exports', 'UrdfCylinder'])
        @Js
        def PyJsHoisted_UrdfVisual_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'rpy', 'pitch', 'geoms', 'origins', 'orientation', 'xyz', 'i', 'roll', 'node', 'options', 'shape', 'position', 'w', 'xml', 'z', 'psi', 'materials', 'the', 'phi', 'x', 'geom', 'yaw', 'type'])
            var.put('xml', var.get('options').get('xml'))
            var.get(u"this").put('origin', var.get(u"null"))
            var.get(u"this").put('geometry', var.get(u"null"))
            var.get(u"this").put('material', var.get(u"null"))
            var.get(u"this").put('name', var.get('options').get('xml').callprop('getAttribute', Js('name')))
            var.put('origins', var.get('xml').callprop('getElementsByTagName', Js('origin')))
            if PyJsStrictEq(var.get('origins').get('length'),Js(0.0)):
                var.get(u"this").put('origin', var.get('Pose').create())
            else:
                var.put('xyz', var.get('origins').get('0').callprop('getAttribute', Js('xyz')))
                var.put('position', var.get('Vector3').create())
                if var.get('xyz'):
                    var.put('xyz', var.get('xyz').callprop('split', Js(' ')))
                    var.put('position', var.get('Vector3').create(Js({'x':var.get('parseFloat')(var.get('xyz').get('0')),'y':var.get('parseFloat')(var.get('xyz').get('1')),'z':var.get('parseFloat')(var.get('xyz').get('2'))})))
                var.put('rpy', var.get('origins').get('0').callprop('getAttribute', Js('rpy')))
                var.put('orientation', var.get('Quaternion').create())
                if var.get('rpy'):
                    var.put('rpy', var.get('rpy').callprop('split', Js(' ')))
                    var.put('roll', var.get('parseFloat')(var.get('rpy').get('0')))
                    var.put('pitch', var.get('parseFloat')(var.get('rpy').get('1')))
                    var.put('yaw', var.get('parseFloat')(var.get('rpy').get('2')))
                    var.put('phi', (var.get('roll')/Js(2.0)))
                    var.put('the', (var.get('pitch')/Js(2.0)))
                    var.put('psi', (var.get('yaw')/Js(2.0)))
                    var.put('x', (((var.get('Math').callprop('sin', var.get('phi'))*var.get('Math').callprop('cos', var.get('the')))*var.get('Math').callprop('cos', var.get('psi')))-((var.get('Math').callprop('cos', var.get('phi'))*var.get('Math').callprop('sin', var.get('the')))*var.get('Math').callprop('sin', var.get('psi')))))
                    var.put('y', (((var.get('Math').callprop('cos', var.get('phi'))*var.get('Math').callprop('sin', var.get('the')))*var.get('Math').callprop('cos', var.get('psi')))+((var.get('Math').callprop('sin', var.get('phi'))*var.get('Math').callprop('cos', var.get('the')))*var.get('Math').callprop('sin', var.get('psi')))))
                    var.put('z', (((var.get('Math').callprop('cos', var.get('phi'))*var.get('Math').callprop('cos', var.get('the')))*var.get('Math').callprop('sin', var.get('psi')))-((var.get('Math').callprop('sin', var.get('phi'))*var.get('Math').callprop('sin', var.get('the')))*var.get('Math').callprop('cos', var.get('psi')))))
                    var.put('w', (((var.get('Math').callprop('cos', var.get('phi'))*var.get('Math').callprop('cos', var.get('the')))*var.get('Math').callprop('cos', var.get('psi')))+((var.get('Math').callprop('sin', var.get('phi'))*var.get('Math').callprop('sin', var.get('the')))*var.get('Math').callprop('sin', var.get('psi')))))
                    var.put('orientation', var.get('Quaternion').create(Js({'x':var.get('x'),'y':var.get('y'),'z':var.get('z'),'w':var.get('w')})))
                    var.get('orientation').callprop('normalize')
                var.get(u"this").put('origin', var.get('Pose').create(Js({'position':var.get('position'),'orientation':var.get('orientation')})))
            var.put('geoms', var.get('xml').callprop('getElementsByTagName', Js('geometry')))
            if (var.get('geoms').get('length')>Js(0.0)):
                var.put('geom', var.get('geoms').get('0'))
                var.put('shape', var.get(u"null"))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('geom').get('childNodes').get('length')):
                    try:
                        var.put('node', var.get('geom').get('childNodes').get(var.get('i')))
                        if PyJsStrictEq(var.get('node').get('nodeType'),Js(1.0)):
                            var.put('shape', var.get('node'))
                            break
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                var.put('type', var.get('shape').get('nodeName'))
                if PyJsStrictEq(var.get('type'),Js('sphere')):
                    var.get(u"this").put('geometry', var.get('UrdfSphere').create(Js({'xml':var.get('shape')})))
                else:
                    if PyJsStrictEq(var.get('type'),Js('box')):
                        var.get(u"this").put('geometry', var.get('UrdfBox').create(Js({'xml':var.get('shape')})))
                    else:
                        if PyJsStrictEq(var.get('type'),Js('cylinder')):
                            var.get(u"this").put('geometry', var.get('UrdfCylinder').create(Js({'xml':var.get('shape')})))
                        else:
                            if PyJsStrictEq(var.get('type'),Js('mesh')):
                                var.get(u"this").put('geometry', var.get('UrdfMesh').create(Js({'xml':var.get('shape')})))
                            else:
                                var.get('console').callprop('warn', (Js('Unknown geometry type ')+var.get('type')))
            var.put('materials', var.get('xml').callprop('getElementsByTagName', Js('material')))
            if (var.get('materials').get('length')>Js(0.0)):
                var.get(u"this").put('material', var.get('UrdfMaterial').create(Js({'xml':var.get('materials').get('0')})))
        PyJsHoisted_UrdfVisual_.func_name = 'UrdfVisual'
        var.put('UrdfVisual', PyJsHoisted_UrdfVisual_)
        var.put('Pose', var.get('require')(Js('../math/Pose')))
        var.put('Vector3', var.get('require')(Js('../math/Vector3')))
        var.put('Quaternion', var.get('require')(Js('../math/Quaternion')))
        var.put('UrdfCylinder', var.get('require')(Js('./UrdfCylinder')))
        var.put('UrdfBox', var.get('require')(Js('./UrdfBox')))
        var.put('UrdfMaterial', var.get('require')(Js('./UrdfMaterial')))
        var.put('UrdfMesh', var.get('require')(Js('./UrdfMesh')))
        var.put('UrdfSphere', var.get('require')(Js('./UrdfSphere')))
        pass
        var.get('module').put('exports', var.get('UrdfVisual'))
    PyJs_anonymous_300_._set_name('anonymous')
    @Js
    def PyJs_anonymous_301_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['module', 'require', 'exports'])
        def PyJs_LONG_302_(var=var):
            return var.get('require')(Js('object-assign'))(Js({'UrdfBox':var.get('require')(Js('./UrdfBox')),'UrdfColor':var.get('require')(Js('./UrdfColor')),'UrdfCylinder':var.get('require')(Js('./UrdfCylinder')),'UrdfLink':var.get('require')(Js('./UrdfLink')),'UrdfMaterial':var.get('require')(Js('./UrdfMaterial')),'UrdfMesh':var.get('require')(Js('./UrdfMesh')),'UrdfModel':var.get('require')(Js('./UrdfModel')),'UrdfSphere':var.get('require')(Js('./UrdfSphere')),'UrdfVisual':var.get('require')(Js('./UrdfVisual'))}), var.get('require')(Js('./UrdfTypes')))
        var.get('module').put('exports', PyJs_LONG_302_())
    PyJs_anonymous_301_._set_name('anonymous')
    @Js
    def PyJs_anonymous_303_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['decodeUint64LE', 'decodeNativeArray', 'cborTypedArrayTagger', 'decodeInt64LE', 'UPPER32', 'warnPrecision', 'warnedPrecision', 'conversionArrayTypes', 'require', 'nativeArrayTypes', 'module', 'exports'])
        @Js
        def PyJsHoisted_warnPrecision_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            if var.get('warnedPrecision').neg():
                var.put('warnedPrecision', Js(True))
                var.get('console').callprop('warn', Js('CBOR 64-bit integer array values may lose precision. No further warnings.'))
        PyJsHoisted_warnPrecision_.func_name = 'warnPrecision'
        var.put('warnPrecision', PyJsHoisted_warnPrecision_)
        @Js
        def PyJsHoisted_decodeUint64LE_(bytes, this, arguments, var=var):
            var = Scope({'bytes':bytes, 'this':this, 'arguments':arguments}, var)
            var.registers(['buffer', 'hi', 'si', 'arr', 'offset', 'byteLen', 'arrLen', 'bytes', 'uint32View', 'i', 'lo'])
            var.get('warnPrecision')()
            var.put('byteLen', var.get('bytes').get('byteLength'))
            var.put('offset', var.get('bytes').get('byteOffset'))
            var.put('arrLen', (var.get('byteLen')/Js(8.0)))
            var.put('buffer', var.get('bytes').get('buffer').callprop('slice', var.get('offset'), (var.get('offset')+var.get('byteLen'))))
            var.put('uint32View', var.get('Uint32Array').create(var.get('buffer')))
            var.put('arr', var.get('Array').create(var.get('arrLen')))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('arrLen')):
                try:
                    var.put('si', (var.get('i')*Js(2.0)))
                    var.put('lo', var.get('uint32View').get(var.get('si')))
                    var.put('hi', var.get('uint32View').get((var.get('si')+Js(1.0))))
                    var.get('arr').put(var.get('i'), (var.get('lo')+(var.get('UPPER32')*var.get('hi'))))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            return var.get('arr')
        PyJsHoisted_decodeUint64LE_.func_name = 'decodeUint64LE'
        var.put('decodeUint64LE', PyJsHoisted_decodeUint64LE_)
        @Js
        def PyJsHoisted_decodeInt64LE_(bytes, this, arguments, var=var):
            var = Scope({'bytes':bytes, 'this':this, 'arguments':arguments}, var)
            var.registers(['buffer', 'hi', 'si', 'arr', 'offset', 'byteLen', 'arrLen', 'int32View', 'bytes', 'uint32View', 'i', 'lo'])
            var.get('warnPrecision')()
            var.put('byteLen', var.get('bytes').get('byteLength'))
            var.put('offset', var.get('bytes').get('byteOffset'))
            var.put('arrLen', (var.get('byteLen')/Js(8.0)))
            var.put('buffer', var.get('bytes').get('buffer').callprop('slice', var.get('offset'), (var.get('offset')+var.get('byteLen'))))
            var.put('uint32View', var.get('Uint32Array').create(var.get('buffer')))
            var.put('int32View', var.get('Int32Array').create(var.get('buffer')))
            var.put('arr', var.get('Array').create(var.get('arrLen')))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('arrLen')):
                try:
                    var.put('si', (var.get('i')*Js(2.0)))
                    var.put('lo', var.get('uint32View').get(var.get('si')))
                    var.put('hi', var.get('int32View').get((var.get('si')+Js(1.0))))
                    var.get('arr').put(var.get('i'), (var.get('lo')+(var.get('UPPER32')*var.get('hi'))))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            return var.get('arr')
        PyJsHoisted_decodeInt64LE_.func_name = 'decodeInt64LE'
        var.put('decodeInt64LE', PyJsHoisted_decodeInt64LE_)
        @Js
        def PyJsHoisted_decodeNativeArray_(bytes, ArrayType, this, arguments, var=var):
            var = Scope({'bytes':bytes, 'ArrayType':ArrayType, 'this':this, 'arguments':arguments}, var)
            var.registers(['buffer', 'offset', 'byteLen', 'bytes', 'ArrayType'])
            var.put('byteLen', var.get('bytes').get('byteLength'))
            var.put('offset', var.get('bytes').get('byteOffset'))
            var.put('buffer', var.get('bytes').get('buffer').callprop('slice', var.get('offset'), (var.get('offset')+var.get('byteLen'))))
            return var.get('ArrayType').create(var.get('buffer'))
        PyJsHoisted_decodeNativeArray_.func_name = 'decodeNativeArray'
        var.put('decodeNativeArray', PyJsHoisted_decodeNativeArray_)
        @Js
        def PyJsHoisted_cborTypedArrayTagger_(data, tag, this, arguments, var=var):
            var = Scope({'data':data, 'tag':tag, 'this':this, 'arguments':arguments}, var)
            var.registers(['tag', 'arrayType', 'data'])
            if var.get('nativeArrayTypes').contains(var.get('tag')):
                var.put('arrayType', var.get('nativeArrayTypes').get(var.get('tag')))
                return var.get('decodeNativeArray')(var.get('data'), var.get('arrayType'))
            if var.get('conversionArrayTypes').contains(var.get('tag')):
                return var.get('conversionArrayTypes').callprop(var.get('tag'), var.get('data'))
            return var.get('data')
        PyJsHoisted_cborTypedArrayTagger_.func_name = 'cborTypedArrayTagger'
        var.put('cborTypedArrayTagger', PyJsHoisted_cborTypedArrayTagger_)
        Js('use strict')
        var.put('UPPER32', var.get('Math').callprop('pow', Js(2.0), Js(32.0)))
        var.put('warnedPrecision', Js(False))
        pass
        pass
        pass
        pass
        var.put('nativeArrayTypes', Js({'64':var.get('Uint8Array'),'69':var.get('Uint16Array'),'70':var.get('Uint32Array'),'72':var.get('Int8Array'),'77':var.get('Int16Array'),'78':var.get('Int32Array'),'85':var.get('Float32Array'),'86':var.get('Float64Array')}))
        var.put('conversionArrayTypes', Js({'71':var.get('decodeUint64LE'),'79':var.get('decodeInt64LE')}))
        pass
        if (PyJsStrictNeq(var.get('module',throw=False).typeof(),Js('undefined')) and var.get('module').get('exports')):
            var.get('module').put('exports', var.get('cborTypedArrayTagger'))
    PyJs_anonymous_303_._set_name('anonymous')
    @Js
    def PyJs_anonymous_304_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['module', 'require', 'exports'])
        var.get('exports').put('DOMImplementation', var.get('window').get('DOMImplementation'))
        var.get('exports').put('XMLSerializer', var.get('window').get('XMLSerializer'))
        var.get('exports').put('DOMParser', var.get('window').get('DOMParser'))
    PyJs_anonymous_304_._set_name('anonymous')
    @Js
    def PyJs_anonymous_305_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['module', 'require', 'exports'])
        var.get('module').put('exports', (var.get('window').get('WebSocket') if PyJsStrictNeq(var.get('window',throw=False).typeof(),Js('undefined')) else var.get('WebSocket')))
    PyJs_anonymous_305_._set_name('anonymous')
    @Js
    def PyJs_anonymous_306_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['module', 'require', 'exports'])
        @Js
        def PyJs_Canvas_307_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments, 'Canvas':PyJs_Canvas_307_}, var)
            var.registers([])
            return var.get('document').callprop('createElement', Js('canvas'))
        PyJs_Canvas_307_._set_name('Canvas')
        var.get('module').put('exports', PyJs_Canvas_307_)
    PyJs_anonymous_306_._set_name('anonymous')
    @Js
    def PyJs_anonymous_308_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['Canvas', 'Image', 'decompressPng', 'require', 'module', 'exports'])
        @Js
        def PyJsHoisted_decompressPng_(data, callback, this, arguments, var=var):
            var = Scope({'data':data, 'callback':callback, 'this':this, 'arguments':arguments}, var)
            var.registers(['callback', 'image', 'data'])
            var.put('image', var.get('Image').create())
            @Js
            def PyJs_anonymous_309_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers(['jsonData', 'canvas', 'imageData', 'i', 'context'])
                var.put('canvas', var.get('Canvas').create())
                var.put('context', var.get('canvas').callprop('getContext', Js('2d')))
                var.get('canvas').put('width', var.get('image').get('width'))
                var.get('canvas').put('height', var.get('image').get('height'))
                var.get('context').put('imageSmoothingEnabled', Js(False))
                var.get('context').put('webkitImageSmoothingEnabled', Js(False))
                var.get('context').put('mozImageSmoothingEnabled', Js(False))
                var.get('context').callprop('drawImage', var.get('image'), Js(0.0), Js(0.0))
                var.put('imageData', var.get('context').callprop('getImageData', Js(0.0), Js(0.0), var.get('image').get('width'), var.get('image').get('height')).get('data'))
                var.put('jsonData', Js(''))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('imageData').get('length')):
                    try:
                        var.put('jsonData', var.get('String').callprop('fromCharCode', var.get('imageData').get(var.get('i')), var.get('imageData').get((var.get('i')+Js(1.0))), var.get('imageData').get((var.get('i')+Js(2.0)))), '+')
                    finally:
                            var.put('i', Js(4.0), '+')
                var.get('callback')(var.get('JSON').callprop('parse', var.get('jsonData')))
            PyJs_anonymous_309_._set_name('anonymous')
            var.get('image').put('onload', PyJs_anonymous_309_)
            var.get('image').put('src', (Js('data:image/png;base64,')+var.get('data')))
        PyJsHoisted_decompressPng_.func_name = 'decompressPng'
        var.put('decompressPng', PyJsHoisted_decompressPng_)
        Js('use strict')
        var.put('Canvas', var.get('require')(Js('canvas')))
        var.put('Image', (var.get('Canvas').get('Image') or var.get('window').get('Image')))
        pass
        var.get('module').put('exports', var.get('decompressPng'))
    PyJs_anonymous_308_._set_name('anonymous')
    @Js
    def PyJs_anonymous_310_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['require', 'module', 'work', 'WorkerSocket', 'workerSocketImpl', 'exports'])
        @Js
        def PyJsHoisted_WorkerSocket_(uri, this, arguments, var=var):
            var = Scope({'uri':uri, 'this':this, 'arguments':arguments}, var)
            var.registers(['uri'])
            var.get(u"this").put('socket_', var.get('work')(var.get('workerSocketImpl')))
            var.get(u"this").get('socket_').callprop('addEventListener', Js('message'), var.get(u"this").get('handleWorkerMessage_').callprop('bind', var.get(u"this")))
            var.get(u"this").get('socket_').callprop('postMessage', Js({'uri':var.get('uri')}))
        PyJsHoisted_WorkerSocket_.func_name = 'WorkerSocket'
        var.put('WorkerSocket', PyJsHoisted_WorkerSocket_)
        try:
            var.put('work', var.get('require')(Js('webworkify')))
        except PyJsException as PyJsTempException:
            PyJsHolder_5265666572656e63654572726f72_3012129 = var.own.get('ReferenceError')
            var.force_own_put('ReferenceError', PyExceptionToJs(PyJsTempException))
            try:
                var.put('work', var.get('require')(Js('webworkify-webpack')))
            finally:
                if PyJsHolder_5265666572656e63654572726f72_3012129 is not None:
                    var.own['ReferenceError'] = PyJsHolder_5265666572656e63654572726f72_3012129
                else:
                    del var.own['ReferenceError']
                del PyJsHolder_5265666572656e63654572726f72_3012129
        var.put('workerSocketImpl', var.get('require')(Js('./workerSocketImpl')))
        pass
        @Js
        def PyJs_anonymous_311_(ev, this, arguments, var=var):
            var = Scope({'ev':ev, 'this':this, 'arguments':arguments}, var)
            var.registers(['data', 'type', 'ev'])
            var.put('data', var.get('ev').get('data'))
            if (var.get('data').instanceof(var.get('ArrayBuffer')) or PyJsStrictEq(var.get('data',throw=False).typeof(),Js('string'))):
                var.get(u"this").callprop('onmessage', var.get('ev'))
            else:
                var.put('type', var.get('data').get('type'))
                if PyJsStrictEq(var.get('type'),Js('close')):
                    var.get(u"this").callprop('onclose', var.get(u"null"))
                else:
                    if PyJsStrictEq(var.get('type'),Js('open')):
                        var.get(u"this").callprop('onopen', var.get(u"null"))
                    else:
                        if PyJsStrictEq(var.get('type'),Js('error')):
                            var.get(u"this").callprop('onerror', var.get(u"null"))
                        else:
                            PyJsTempException = JsToPyException(Js('Unknown message from workersocket'))
                            raise PyJsTempException
        PyJs_anonymous_311_._set_name('anonymous')
        var.get('WorkerSocket').get('prototype').put('handleWorkerMessage_', PyJs_anonymous_311_)
        @Js
        def PyJs_anonymous_312_(data, this, arguments, var=var):
            var = Scope({'data':data, 'this':this, 'arguments':arguments}, var)
            var.registers(['data'])
            var.get(u"this").get('socket_').callprop('postMessage', var.get('data'))
        PyJs_anonymous_312_._set_name('anonymous')
        var.get('WorkerSocket').get('prototype').put('send', PyJs_anonymous_312_)
        @Js
        def PyJs_anonymous_313_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            var.get(u"this").get('socket_').callprop('postMessage', Js({'close':Js(True)}))
        PyJs_anonymous_313_._set_name('anonymous')
        var.get('WorkerSocket').get('prototype').put('close', PyJs_anonymous_313_)
        var.get('module').put('exports', var.get('WorkerSocket'))
    PyJs_anonymous_310_._set_name('anonymous')
    @Js
    def PyJs_anonymous_314_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['module', 'require', 'exports', 'WebSocket'])
        var.put('WebSocket', (var.get('WebSocket') or var.get('require')(Js('ws'))))
        @Js
        def PyJs_anonymous_315_(self, this, arguments, var=var):
            var = Scope({'self':self, 'this':this, 'arguments':arguments}, var)
            var.registers(['self', 'handleSocketControl', 'socket', 'handleSocketMessage'])
            @Js
            def PyJsHoisted_handleSocketMessage_(ev, this, arguments, var=var):
                var = Scope({'ev':ev, 'this':this, 'arguments':arguments}, var)
                var.registers(['data', 'ev'])
                var.put('data', var.get('ev').get('data'))
                if var.get('data').instanceof(var.get('ArrayBuffer')):
                    var.get('self').callprop('postMessage', var.get('data'), Js([var.get('data')]))
                else:
                    var.get('self').callprop('postMessage', var.get('data'))
            PyJsHoisted_handleSocketMessage_.func_name = 'handleSocketMessage'
            var.put('handleSocketMessage', PyJsHoisted_handleSocketMessage_)
            @Js
            def PyJsHoisted_handleSocketControl_(ev, this, arguments, var=var):
                var = Scope({'ev':ev, 'this':this, 'arguments':arguments}, var)
                var.registers(['ev'])
                var.get('self').callprop('postMessage', Js({'type':var.get('ev').get('type')}))
            PyJsHoisted_handleSocketControl_.func_name = 'handleSocketControl'
            var.put('handleSocketControl', PyJsHoisted_handleSocketControl_)
            var.put('socket', var.get(u"null"))
            pass
            pass
            @Js
            def PyJs_anonymous_316_(ev, this, arguments, var=var):
                var = Scope({'ev':ev, 'this':this, 'arguments':arguments}, var)
                var.registers(['data', 'ev', 'uri'])
                var.put('data', var.get('ev').get('data'))
                if PyJsStrictEq(var.get('data',throw=False).typeof(),Js('string')):
                    var.get('socket').callprop('send', var.get('data'))
                else:
                    if var.get('data').callprop('hasOwnProperty', Js('close')):
                        var.get('socket').callprop('close')
                        var.put('socket', var.get(u"null"))
                    else:
                        if var.get('data').callprop('hasOwnProperty', Js('uri')):
                            var.put('uri', var.get('data').get('uri'))
                            var.put('socket', var.get('WebSocket').create(var.get('uri')))
                            var.get('socket').put('binaryType', Js('arraybuffer'))
                            var.get('socket').put('onmessage', var.get('handleSocketMessage'))
                            var.get('socket').put('onclose', var.get('handleSocketControl'))
                            var.get('socket').put('onopen', var.get('handleSocketControl'))
                            var.get('socket').put('onerror', var.get('handleSocketControl'))
                        else:
                            PyJsTempException = JsToPyException(Js('Unknown message to WorkerSocket'))
                            raise PyJsTempException
            PyJs_anonymous_316_._set_name('anonymous')
            var.get('self').callprop('addEventListener', Js('message'), PyJs_anonymous_316_)
        PyJs_anonymous_315_._set_name('anonymous')
        var.get('module').put('exports', PyJs_anonymous_315_)
    PyJs_anonymous_314_._set_name('anonymous')
    @Js
    def PyJs_anonymous_317_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['r'])
        @Js
        def PyJsHoisted_r_(e, n, t, this, arguments, var=var):
            var = Scope({'e':e, 'n':n, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'e', 'n', 'u', 'o', 'i'])
            @Js
            def PyJsHoisted_o_(i, f, this, arguments, var=var):
                var = Scope({'i':i, 'f':f, 'this':this, 'arguments':arguments}, var)
                var.registers(['a', 'c', 'f', 'p', 'i'])
                if var.get('n').get(var.get('i')).neg():
                    if var.get('e').get(var.get('i')).neg():
                        var.put('c', ((Js('function')==var.get('require',throw=False).typeof()) and var.get('require')))
                        if (var.get('f').neg() and var.get('c')):
                            return var.get('c')(var.get('i'), Js(0.0).neg())
                        if var.get('u'):
                            return var.get('u')(var.get('i'), Js(0.0).neg())
                        var.put('a', var.get('Error').create(((Js("Cannot find module '")+var.get('i'))+Js("'"))))
                        PyJsTempException = JsToPyException(PyJsComma(var.get('a').put('code', Js('MODULE_NOT_FOUND')),var.get('a')))
                        raise PyJsTempException
                    var.put('p', var.get('n').put(var.get('i'), Js({'exports':Js({})})))
                    @Js
                    def PyJs_anonymous_318_(r, this, arguments, var=var):
                        var = Scope({'r':r, 'this':this, 'arguments':arguments}, var)
                        var.registers(['r', 'n'])
                        var.put('n', var.get('e').get(var.get('i')).get('1').get(var.get('r')))
                        return var.get('o')((var.get('n') or var.get('r')))
                    PyJs_anonymous_318_._set_name('anonymous')
                    var.get('e').get(var.get('i')).get('0').callprop('call', var.get('p').get('exports'), PyJs_anonymous_318_, var.get('p'), var.get('p').get('exports'), var.get('r'), var.get('e'), var.get('n'), var.get('t'))
                return var.get('n').get(var.get('i')).get('exports')
            PyJsHoisted_o_.func_name = 'o'
            var.put('o', PyJsHoisted_o_)
            pass
            #for JS loop
            var.put('u', ((Js('function')==var.get('require',throw=False).typeof()) and var.get('require')))
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('t').get('length')):
                try:
                    var.get('o')(var.get('t').get(var.get('i')))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            return var.get('o')
        PyJsHoisted_r_.func_name = 'r'
        var.put('r', PyJsHoisted_r_)
        pass
        return var.get('r')
    PyJs_anonymous_317_._set_name('anonymous')
    return PyJs_anonymous_317_()(Js({'1':Js([PyJs_anonymous_0_, Js({})]),'2':Js([PyJs_anonymous_4_, Js({'_process':Js(4.0),'timers':Js(5.0)})]),'3':Js([PyJs_anonymous_70_, Js({})]),'4':Js([PyJs_anonymous_74_, Js({})]),'5':Js([PyJs_anonymous_83_, Js({'process/browser.js':Js(4.0),'timers':Js(5.0)})]),'6':Js([PyJs_anonymous_98_, Js({})]),'7':Js([PyJs_anonymous_113_, Js({})]),'8':Js([PyJs_anonymous_116_, Js({'./actionlib':Js(14.0),'./core':Js(23.0),'./math':Js(28.0),'./tf':Js(31.0),'./urdf':Js(43.0),'object-assign':Js(3.0)})]),'9':Js([PyJs_anonymous_117_, Js({'./RosLib':Js(8.0)})]),'10':Js([PyJs_anonymous_120_, Js({'../core/Message':Js(15.0),'../core/Topic':Js(22.0),'eventemitter2':Js(2.0)})]),'11':Js([PyJs_anonymous_128_, Js({'../core/Message':Js(15.0),'../core/Topic':Js(22.0),'eventemitter2':Js(2.0)})]),'12':Js([PyJs_anonymous_134_, Js({'../core/Message':Js(15.0),'eventemitter2':Js(2.0)})]),'13':Js([PyJs_anonymous_141_, Js({'../core/Message':Js(15.0),'../core/Topic':Js(22.0),'eventemitter2':Js(2.0)})]),'14':Js([PyJs_anonymous_150_, Js({'../core/Ros':Js(17.0),'../mixin':Js(29.0),'./ActionClient':Js(10.0),'./ActionListener':Js(11.0),'./Goal':Js(12.0),'./SimpleActionServer':Js(13.0)})]),'15':Js([PyJs_anonymous_151_, Js({'object-assign':Js(3.0)})]),'16':Js([PyJs_anonymous_152_, Js({'./Service':Js(18.0),'./ServiceRequest':Js(19.0)})]),'17':Js([PyJs_anonymous_157_, Js({'../util/workerSocket':Js(49.0),'./Service':Js(18.0),'./ServiceRequest':Js(19.0),'./SocketAdapter.js':Js(21.0),'eventemitter2':Js(2.0),'object-assign':Js(3.0),'ws':Js(46.0)})]),'18':Js([PyJs_anonymous_226_, Js({'./ServiceRequest':Js(19.0),'./ServiceResponse':Js(20.0),'eventemitter2':Js(2.0)})]),'19':Js([PyJs_anonymous_232_, Js({'object-assign':Js(3.0)})]),'20':Js([PyJs_anonymous_233_, Js({'object-assign':Js(3.0)})]),'21':Js([PyJs_anonymous_234_, Js({'../util/cborTypedArrayTags':Js(44.0),'../util/decompressPng':Js(48.0),'cbor-js':Js(1.0)})]),'22':Js([PyJs_anonymous_242_, Js({'./Message':Js(15.0),'eventemitter2':Js(2.0)})]),'23':Js([PyJs_anonymous_253_, Js({'../mixin':Js(29.0),'./Message':Js(15.0),'./Param':Js(16.0),'./Ros':Js(17.0),'./Service':Js(18.0),'./ServiceRequest':Js(19.0),'./ServiceResponse':Js(20.0),'./Topic':Js(22.0)})]),'24':Js([PyJs_anonymous_254_, Js({'./Quaternion':Js(25.0),'./Vector3':Js(27.0)})]),'25':Js([PyJs_anonymous_259_, Js({})]),'26':Js([PyJs_anonymous_266_, Js({'./Quaternion':Js(25.0),'./Vector3':Js(27.0)})]),'27':Js([PyJs_anonymous_268_, Js({})]),'28':Js([PyJs_anonymous_273_, Js({'./Pose':Js(24.0),'./Quaternion':Js(25.0),'./Transform':Js(26.0),'./Vector3':Js(27.0)})]),'29':Js([PyJs_anonymous_274_, Js({})]),'30':Js([PyJs_anonymous_278_, Js({'../actionlib/ActionClient':Js(10.0),'../actionlib/Goal':Js(12.0),'../core/Service.js':Js(18.0),'../core/ServiceRequest.js':Js(19.0),'../core/Topic.js':Js(22.0),'../math/Transform':Js(26.0)})]),'31':Js([PyJs_anonymous_287_, Js({'../core/Ros':Js(17.0),'../mixin':Js(29.0),'./TFClient':Js(30.0)})]),'32':Js([PyJs_anonymous_288_, Js({'../math/Vector3':Js(27.0),'./UrdfTypes':Js(41.0)})]),'33':Js([PyJs_anonymous_289_, Js({})]),'34':Js([PyJs_anonymous_290_, Js({'./UrdfTypes':Js(41.0)})]),'35':Js([PyJs_anonymous_291_, Js({'../math/Pose':Js(24.0),'../math/Quaternion':Js(25.0),'../math/Vector3':Js(27.0)})]),'36':Js([PyJs_anonymous_292_, Js({'./UrdfVisual':Js(42.0)})]),'37':Js([PyJs_anonymous_293_, Js({'./UrdfColor':Js(33.0),'object-assign':Js(3.0)})]),'38':Js([PyJs_anonymous_296_, Js({'../math/Vector3':Js(27.0),'./UrdfTypes':Js(41.0)})]),'39':Js([PyJs_anonymous_297_, Js({'./UrdfJoint':Js(35.0),'./UrdfLink':Js(36.0),'./UrdfMaterial':Js(37.0),'@xmldom/xmldom':Js(45.0)})]),'40':Js([PyJs_anonymous_298_, Js({'./UrdfTypes':Js(41.0)})]),'41':Js([PyJs_anonymous_299_, Js({})]),'42':Js([PyJs_anonymous_300_, Js({'../math/Pose':Js(24.0),'../math/Quaternion':Js(25.0),'../math/Vector3':Js(27.0),'./UrdfBox':Js(32.0),'./UrdfCylinder':Js(34.0),'./UrdfMaterial':Js(37.0),'./UrdfMesh':Js(38.0),'./UrdfSphere':Js(40.0)})]),'43':Js([PyJs_anonymous_301_, Js({'./UrdfBox':Js(32.0),'./UrdfColor':Js(33.0),'./UrdfCylinder':Js(34.0),'./UrdfLink':Js(36.0),'./UrdfMaterial':Js(37.0),'./UrdfMesh':Js(38.0),'./UrdfModel':Js(39.0),'./UrdfSphere':Js(40.0),'./UrdfTypes':Js(41.0),'./UrdfVisual':Js(42.0),'object-assign':Js(3.0)})]),'44':Js([PyJs_anonymous_303_, Js({})]),'45':Js([PyJs_anonymous_304_, Js({})]),'46':Js([PyJs_anonymous_305_, Js({})]),'47':Js([PyJs_anonymous_306_, Js({})]),'48':Js([PyJs_anonymous_308_, Js({'canvas':Js(47.0)})]),'49':Js([PyJs_anonymous_310_, Js({'./workerSocketImpl':Js(50.0),'webworkify':Js(7.0),'webworkify-webpack':Js(6.0)})]),'50':Js([PyJs_anonymous_314_, Js({'ws':Js(46.0)})])}), Js({}), Js([Js(9.0)]))
PyJs_LONG_319_()
pass


# Add lib to the module scope
roslib = var.to_python()