export default class HolbertonClass {
    consructor(size, loation) {
        this.size = size;
        this.location = location;
}

[Symbol.toPrimitive](hint) {
    if (hint === 'string') {
        return this.location;
}
if (hint === 'number') {
    return this.size;
}

return this;
}
}