from flask import Markup

# GAMEDATA['gamestate'] :   0 - no game in progress
#                           1 - there is a player, no bankroll
#                           2 - bankroll set, no bet
#                           3 - bet set, initial cards have been dealt
#                           4 - kept, resolved, no new bet
def handler(data):
    gs = data.gamestate
    if gs == 1:
        output = '<p>Please choose a starting bankroll and bet denomination.</p>'
        output += '''
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
        </form>'''
    if gs == 2:
        if data.denom >= 100:
            d = '${}'.format(int(data.denom/100))
        else:
            d = '{}¢'.format(data.denom)
        output = '<p>You are starting off with a bankroll of ${}. You are \
            betting {} per coin, so you have {} credits.</p>'.format(
            data.bankroll//100, d, int(data.bankroll/data.denom))

    output += '''<br /><br />
        <form action="" method="post">
            <input type="submit" name="quit" value="Quit" />
        </form>
        '''
    output = Markup(output)
    if gs == 0:
        output = 'ERROR! NO GAME IN PROGRESS.'
    return output
