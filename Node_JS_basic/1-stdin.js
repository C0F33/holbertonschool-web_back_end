const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const question = (query) => {
    return new Promise((resolve) => rl.question(query, resolve));
};

(async () => {
    console.log('Welcome to Holberton School, what is your name?');
    const name = await question('');
    console.log(`Your name is: ${name}`);
    rl.close();
})();

rl.on('close', () => {
    console.log('This important software is now closing');
    process.exit(0);
});
