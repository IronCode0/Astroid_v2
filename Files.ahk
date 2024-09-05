#Requires AutoHotkey v2.0

z :=["-s","800x480","-t","black","-f","F:\new.txt"]
msgbox Arg_Pharse(z)
Arg_Pharse(input,start :=0,end :=-1) {
    output :={0:"DEFAULT"}
    param :=""
    ;words :=StrSplit(input," ")
    for idx in input
    {
        if (A_index < start)
            continue
        word := idx
        if (substr(word,1,1) == "-") {
            param := substr(word,2)
            msgbox param
            output.append({param:[]})
            ;output[param] := ["DEFAULT"]
        } else {
            if (param == "")
                continue
            else
                output[param].append(word)
        }
    }

    return output
}
exitapp


