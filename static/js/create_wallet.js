/**
 * Created by ne_luboff on 19.07.18.
 */


function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

window.onload = ( function(){
    var password = getParameterByName('p');
    if(password == null || password == '') {
        password = "test";
    }
    var randomSeed = lightwallet.keystore.generateRandomSeed();

    lightwallet.keystore.createVault({password: password, seedPhrase: randomSeed, hdPathString: "m/44'/60'/0'/0"}, function (err, ks) {
        ks.keyFromPassword(password, function(err, pwDerivedKey) {
            ks.generateNewAddress(pwDerivedKey);

            var address = ks.getAddresses();
            var key = ks.exportPrivateKey(address[0], pwDerivedKey);

			var data = JSON.stringify({address:address[0],seed:randomSeed,privateKey:key,password:password}, null, 2);
            document.getElementById("data").innerHTML += data;
        })
    })
});