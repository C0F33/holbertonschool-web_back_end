const fs = require('fs');

function countStudents(path) {
    try {
        const data = fs.readFileSync(path, 'utf8');
        const lines = data.split('\n').filter(line => line.trim() !== '');

        if (lines.length <= 1) {
            console.log('Number of students: 0');
            return;
        }

        const headers = lines[0].split(',');
        const students = lines.slice(1).map(line => line.split(','));

        const fields = students.reduce((acc, student) => {
            const field = student[headers.indexOf('field')];
            const firstName = student[headers.indexOf('firstname')];
            if (!acc[field]) acc[field] = [];
            acc[field].push(firstName);
            return acc;
        }, {});

        console.log(`Number of students: ${students.length}`);
        for (const [field, names] of Object.entries(fields)) {
            console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
        }
    } catch (err) {
        throw new Error('Cannot load the database');
    }
}
