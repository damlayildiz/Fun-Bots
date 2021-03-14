const Discord = require('discord.js');
const client = new Discord.Client();

client.once('ready', () => {
	console.log('Ready!');
});

client.on('message', message => {
	if (message.content.includes('!isTodayBday smol')) {
        var today = new Date();
        var day = today.getDate();
        var month = today.getMonth();
        if (day == 23 && month == 0){
            message.channel.send('YES! Happy Birthday smol');
        } else {
            message.channel.send('Nope!');
        }
    } 
    if (message.content.includes('!isTodayBday big')) {
        var today = new Date();
        var day = today.getDate();
        var month = today.getMonth();
        if (day == 8 && month == 1){
            message.channel.send('YES! Happy Birthday big');
        } else {
            message.channel.send('Nope!');
        }
    }

    if (message.content.includes('!isTodayBday midyum')) {
        var today = new Date();
        var day = today.getDate();
        var month = today.getMonth();
        if (day == 19 && month == 2){
            message.channel.send('YES! Happy Birthday midyum');
        } else {
            message.channel.send('Nope!');
        }
    }

    if (message.content.includes('!isTodayBday capon')) {
        var today = new Date();
        var day = today.getDate();
        var month = today.getMonth();
        if (day == 31 && month == 6){
            message.channel.send('YES! Happy Birthday capon');
        } else {
            message.channel.send('Nope!');
        }
    }
});

client.login('ODAyMjA5NTY5ODcwMDUzNDE2.YAr54Q.ERtO4MpU-u4zHuoPueYBnMva2Pc');
