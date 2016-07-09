player_no_bankroll = '''
<p>Please choose a starting bankroll and bet denomination.</p>
<form action="" method="post" onsubmit="broll.value=parseInt(b.value)">
<table id="poker">
    <tr>
        <td>Add bills:</td>
        <td>
            <button type="button" id="f" value="5" onclick="b.value=parseInt(b.value)+parseInt(f.value)">$5</button>
            <button type="button" id="t" value="20" onclick="b.value=parseInt(b.value)+parseInt(t.value)">$20</button>
            <button type="button" id="h" value="100" onclick="b.value=parseInt(b.value)+parseInt(h.value)">$100</button>
        </td>
    </tr>
    <tr>
        <td style="padding-top:9px;">Bankroll: $</td>
        <td><output name="b" for="f t h r">0</output>
        <input name="broll" style="display:none;" /></td>
    </tr>
    <tr>
        <td>Bet denomination:</td>
        <td style="padding-top:20px;">
            <select name="denom">
                <option value="5">5¢</option>
                <option value="10">10¢</option>
                <option value="25">25¢</option>
                <option value="50">50¢</option>
                <option value="100">$1</option>
                <option value="500">$5</option>
            </select><br /><br />
        </td>
    </tr>
</table>
<input type="submit" value="Start!" /> <button type="button" id="r" onclick="b.value=0">Reset bankroll to zero</button>
</form>
'''

gametable = '''
<form id="p_main" action="" method="post" onsubmit="thebet.value=parseInt(bet.value)">
<table id="p_game">
    <tr>
        <td colspan="6">paytable</td>
    </tr>
    <tr class="p_cards">
        <td> </td>
        {cards}
    </tr>
    <tr id="p_cards">
        {checkboxes}
    </tr>
    </tr>
    <tr class="p_text">
        <td> </td>
        <td> </td>
        <td>win</td>
        <td>
        <table style="margin:0 auto;"><tr><td style="padding-top:7px;">Bet&nbsp;</td><td><output name="bet" for="b1 bm" style="font-size:14pt;">{betamt}</outcome></td></tr></table>
        </td>
        <td>{creds}</td>
        <td> </td>
    </tr>
    <tr class="p_text">
        <td> </td>
        <td> </td>
        <td>{hand}</td>
        <td>{invis}</td>
        <td>${bank}</td>
        <td> </td>
    </tr>
    <tr>
        <td style="colspan:6;padding:15px;"></td>
    </tr>
    <tr class="p_text">
        <td> </td>
        <td> </td>
        <td>{betone}</td>
        <td>{betmax}</td>
        <td>{deal}</td>
        <td> </td>
    </tr>
</table>
</form>
'''

betone = '<button type="button" id="b1" value="1" onclick="if(parseInt(bet.value)==5){{bet.value=1}}else{{bet.value=parseInt(bet.value)+1}}">Bet 1</button>'
betmax = '<button type="button" id="bm" onclick="bet.value=5;">Bet Max</button>'

invis = '<input name="thebet" style="display:none;" />'

deal = '<input type="submit" name="deal" value="Deal" />'
redeal = '<input type="submit" name="redeal" value="Deal" />'

checkboxes = '''
        <td>Keep:</td>
        <td><input type="checkbox" name="keep" value"1" /></td>
        <td><input type="checkbox" name="keep" value"2" /></td>
        <td><input type="checkbox" name="keep" value"3" /></td>
        <td><input type="checkbox" name="keep" value"4" /></td>
        <td><input type="checkbox" name="keep" value"5" /></td>
'''

no_checkboxes = '''
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
'''

quit = '''
<br /><br />
    <form action="" method="post">
        <input type="submit" name="quit" value="Quit" />
    </form>
'''