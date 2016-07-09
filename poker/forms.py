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
<form action="" method="post">
<table id="p_game">
    <tr>
        <td colspan="6">paytable</td>
    </tr>
    <tr class="p_cards">
        <td> </td>
        {cards}
    </tr>
    <tr id="p_cards">
        <td>Keep:</td>
        {checkboxes}
    </tr>
    </tr>
    <tr>
        <td> </td>
        <td> </td>
        <td>win</td>
        <td>bet</td>
        <td>creds</td>
        <td> </td>
    </tr>
    <tr>
        <td> </td>
        <td> </td>
        <td>hand</td>
        <td>(invis)</td>
        <td>$bank</td>
        <td> </td>
    </tr>
    <tr>
        <td> </td>
        <td> </td>
        <td>bet 1</td>
        <td>bet max</td>
        <td>deal</td>
        <td> </td>
    </tr>
</table>
</form>
'''

checkboxes = '''
        <td><input type="checkbox" name="c1" value"c1" /></td>
        <td><input type="checkbox" name="c2" value"c2" /></td>
        <td><input type="checkbox" name="c3" value"c3" /></td>
        <td><input type="checkbox" name="c4" value"c4" /></td>
        <td><input type="checkbox" name="c5" value"c5" /></td>
'''

no_checkboxes = '''
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