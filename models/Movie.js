'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;
const Mixed = Schema.Types.Mixed;

var movieSchema = Schema( {
    title: String,
    cast : [String],
    year: Number,
    genres: [String],
} );

module.exports = mongoose.model( 'Movie', movieSchema );
