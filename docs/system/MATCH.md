# Event to Repository Matching Algorithm.

This document describes the fields available for routing incoming publications, using Match data extracted from the
metadata and package files, and comparing it with a configuration supplied by the repository to define the match criteria

## Fields in the Match data

The following fields may be extracted from the incoming metadata

* URLs
* Emails
* Affiliations
* Author Identifiers
* Postcodes
* Grants

The following fields are available in the data model, but are not currently used:

* Keywords
* Content Types

## Fields in the Repository Config

The repository configuration may contain the following fields

* Domains
* Name Variants
* Author Identifiers
* Grants
* Arbitrary Strings

The following fields are available in the data model, but are not currently used:

* Keywords
* Content Types
* Postcodes

## Paired fields and analysis required

In each of these paired sets of fields, the criteria for a successful match is defined.  A publication as a whole
will be considered to have been matched to a repository if one or more of these fields matches exactly.

Note that here "exact match" means that the lowercased, whitespace-trimmed strings from each field are the same.

* Domain <-> URL - normalise the domain: strip prefixes and URL paths.  If either ends with the other, it is a match
* Domain <-> Email - normalise the domain: strip prefixes an URL paths.  Normalise the email: strip everything before @.  If either ends with the other it is a match
* Name Variant <-> Affiliation - normalised name variant must be an exact substring of normalised affiliation
* Author Identifier <-> Email - exact match required
* Author Identifier <-> Author Identifier - exact match required
* Grant <-> Grant - exact match required
* Arbitrary String <-> URL - Normalise the String and the URL: strip prefixes and URL paths.  If either ends with the other, it is a match
* Arbitrary String <-> email - exact match required
* Arbitrary String <-> Affiliation - normalised string must be an exact substring of normalised affiliation
* Arbitrary String <-> Author ID - exact match required
* Arbitrary String <-> Grant - exact match requried

The following mappings are also proposed, but are not currently implemented, due to the variable quality of the data
in these fields:

* Keyword <-> Keyword - exact match required
* Content Type <-> Content Type - exact match required
* Postcode <-> Postcode - Normalise postcodes: strip whitespace and lowercase, then exact match required

For some countries, such as Germany, postcodes may not be as geo-locally resolving as it is the case in the UK.  Therefore, we are probably better off to put away this matching option, in general.
