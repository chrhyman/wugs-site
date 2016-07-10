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
        <td><output name="b" for="f t h r" id="b">0</output>
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
        <td colspan="6">
            <table id="pays">
                <tr id="coins">
                    <th>Coins bet:</th>
                    <th>1</th>
                    <th>2</th>
                    <th>3</th>
                    <th>4</th>
                    <th>5</th>
                </tr>
                <tr id="htop">
                    <th class="hand">Royal Flush</th>
                    <td class="kol1">800</td>
                    <td class="kol2">1600</td>
                    <td class="kol3">2400</td>
                    <td class="kol4">3200</td>
                    <td class="kol5">4000</td>
                </tr>
                <tr>
                    <th class="hand">Straight Flush</th>
                    <td class="kol1">50</td>
                    <td class="kol2">100</td>
                    <td class="kol3">150</td>
                    <td class="kol4">200</td>
                    <td class="kol5">250</td>
                </tr>
                <tr>
                    <th class="hand">Four of a Kind</th>
                    <td class="kol1">25</td>
                    <td class="kol2">50</td>
                    <td class="kol3">75</td>
                    <td class="kol4">100</td>
                    <td class="kol5">125</td>
                </tr>
                <tr>
                    <th class="hand">Full House</th>
                    <td class="kol1">9</td>
                    <td class="kol2">18</td>
                    <td class="kol3">27</td>
                    <td class="kol4">36</td>
                    <td class="kol5">45</td>
                </tr>
                <tr>
                    <th class="hand">Flush</th>
                    <td class="kol1">6</td>
                    <td class="kol2">12</td>
                    <td class="kol3">18</td>
                    <td class="kol4">24</td>
                    <td class="kol5">30</td>
                </tr>
                <tr>
                    <th class="hand">Straight</th>
                    <td class="kol1">4</td>
                    <td class="kol2">8</td>
                    <td class="kol3">12</td>
                    <td class="kol4">16</td>
                    <td class="kol5">20</td>
                </tr>
                <tr>
                    <th class="hand">Three of a Kind</th>
                    <td class="kol1">3</td>
                    <td class="kol2">6</td>
                    <td class="kol3">9</td>
                    <td class="kol4">12</td>
                    <td class="kol5">15</td>
                </tr>
                <tr>
                    <th class="hand">Two Pair</th>
                    <td class="kol1">2</td>
                    <td class="kol2">4</td>
                    <td class="kol3">6</td>
                    <td class="kol4">8</td>
                    <td class="kol5">10</td>
                </tr>
                <tr>
                    <th class="hand">Jacks or Better</th>
                    <td class="kol1">1</td>
                    <td class="kol2">2</td>
                    <td class="kol3">3</td>
                    <td class="kol4">4</td>
                    <td class="kol5">5</td>
                </tr>
            </table>
        </td>
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
        <td>{win}</td>
        <td>
        <table style="margin:0 auto;"><tr><td style="padding-top:7px;">Bet&nbsp;</td><td><output name="bet" for="b1 bm" style="font-size:14pt;">{betamt}</outcome></td></tr></table>
        </td>
        <td>{creds} credits</td>
        <td> </td>
    </tr>
    <tr class="p_text" style="height:40px;">
        <td> </td>
        <td> </td>
        <td>{hand}</td>
        <td>{invis}</td>
        <td><p style="font-size:10pt;">${bank}</p></td>
        <td> </td>
    </tr>
    <tr>
        <td style="padding:15px;colspan:6;"></td>
    </tr>
    <tr class="p_text" style="height:50px">
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

betone = '<button type="button" id="b1" value="1" onclick="if(parseInt(bet.value)==5){bet.value=1}else{bet.value=parseInt(bet.value)+1};">Bet 1</button>'
betmax = '<button type="button" id="bm" onclick="bet.value=5;">Bet Max</button>'

invis = '<input name="thebet" style="display:none;" />'

deal = '<input type="submit" name="deal" value="Deal" />'
redeal = '<input type="submit" name="redeal" value="Deal" />'

checkboxes = '''
        <td style="width:55px;">Keep:</td>
        <td><input type="checkbox" id= "c0" name="keep" value="1" /></td>
        <td><input type="checkbox" id= "c1" name="keep" value="2" /></td>
        <td><input type="checkbox" id= "c2" name="keep" value="3" /></td>
        <td><input type="checkbox" id= "c3" name="keep" value="4" /></td>
        <td><input type="checkbox" id= "c4" name="keep" value="5" /></td>
'''

no_checkboxes = '''
        <td style="width:55px;">{kept}</td>
        <td><input type="checkbox" disabled{} /></td>
        <td><input type="checkbox" disabled{} /></td>
        <td><input type="checkbox" disabled{} /></td>
        <td><input type="checkbox" disabled{} /></td>
        <td><input type="checkbox" disabled{} /></td>
'''

quit = '''
<br /><br />
<table><tr><td style="padding-right:10px;">
    <form action="/games/poker/submit" method="post">
        <input type="text" style="display:none;" name="username" value={username} />
        <input type="text" style="display:none;" name="startmoney" value={startmoney} />
        <input type="text" style="display:none;" name="endmoney" value={endmoney} />
        <input type="text" style="display:none;" name="handsplayed" value={handsplayed} />
        <input type="submit" name="submit" value="Submit to Leaderboards!" />
    </form></td><td>
    <form action="" method="post">
        <input type="submit" name="quit" value="Quit" />
    </form></td></tr></table>
'''
