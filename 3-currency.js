export default class Currency
{
    constructor(code, name) {
        if (typeof code === 'string') {
            this._code = code;
        } else {
            throw TypeError('Code must be a string');
        }

        if (typeof name === 'string') {
            this._name = name;
        } else {
            throw TypeError('name must be a string');
        }
    }
}
