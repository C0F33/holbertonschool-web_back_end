export default class Car {
    contructor(brand, motor, color) {
        this._brand = brand;
        this._motor = motor;
        this._color = color;
}
    cloneCar() {
    return new this.constructor();
 }
}