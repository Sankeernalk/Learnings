def flattenjson( b ):
    val = {}
    for i in b.keys():
        if isinstance( b[i], dict ):
            get = flattenjson( b[i] )
            for j in get.keys():
                val[ i + '__' + j ] = get[j]
        else:
            val[i] = b[i]
    return val


final_dict = flattenjson( {
    "a": 1,
    "b": 2,
    "c": [{"d": [2, 3, 4], "e": [{"f": 1, "g": 2}]}]
} )

print(final_dict)

#final_dict = flattenjson({"header":{"platform":"atm","version":"2.0"},"details":[{"abc":"3","def":"4"},{"abc":"5","def":"6"},{"abc":"7","def":"8"}]} )

# dict_json1 = {"header":{"platform":"atm","version":"2.0"},"details":[{"abc":"3","def":"4"},{"abc":"5","def":"6"},{"abc":"7","def":"8"}]}
#
# for i in dict_json1.keys():
#     print(type(dict_json1[i]))
#
# print(final_dict)
