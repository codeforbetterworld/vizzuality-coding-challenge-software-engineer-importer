'use strict'

let chai = require('chai');
let chaiHttp = require('chai-http');
const expect = require('chai').expect;
chai.use(chaiHttp);

const url= 'http://localhost/api/emissions';

describe('Test case >> emissions: ',()=>{

	it('should get all emissions', (done) => {
		chai.request(url)
			.get('/all')
			.end( function(err,res){
                expect(res).to.have.status(200);
                expect(res).to.have.header('content-type', /json/);
                expect(res).to.be.json;
				done();
			});
    });

    it('should get all emissions filtered by Country USA', (done) => {
		chai.request(url)
			.get('/country/USA')
			.end( function(err,res){
                expect(res).to.have.status(200);
                expect(res).to.have.header('content-type', /json/);
                expect(res).to.be.json;
				done();
			});
    });

    it('should get all emissions filtered by Sector Energy', (done) => {
		chai.request(url)
			.get('/sector/Energy')
			.end( function(err,res){
                expect(res).to.have.status(200);
                expect(res).to.have.header('content-type', /json/);
                expect(res).to.be.json;
				done();
			});
    });

    it('should get all emissions filtered by Parent sector Other', (done) => {
		chai.request(url)
			.get('/parentsector/Industrial%20process')
			.end( function(err,res){
                expect(res).to.have.status(200);
                expect(res).to.have.header('content-type', /json/);
                expect(res).to.be.json;
				done();
			});
	});

});