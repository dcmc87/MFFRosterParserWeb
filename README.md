# MFFRosterParserWeb

## Quick Start
- POST screenshots to the supplied endpoint, result returned in JSON  
- JSON format follows https://www.mokhet.com/MFF/


## Technical details
#### File uploads  
* Most image sizes should work now that Tesseract is trained, tested with width 800 & above
  * I'm currently using this library for image compression : https://www.npmjs.com/package/compress.js
  * with settings <100kB, quality 0.85, maxWidth/Height 2000, resize true
  * any compression method which preserves image resolution with decent quality should work
* Working resolutions
  * 16:9, 16:10, 4:3, 18.5:9, will add 3:2 soon, accepting requests
* Accepted file formats  
  * PNG, JPG, GIF, BMP, TIFF
* Data should be POSTed in FormData object, with attribute "file"
    ```javascript
    var formData = new FormData();  
    .....  
    .....  
    formData.append("file", file)
    
    ```
* Max request limit : 15 MB
* CORS should hopefully be working

#### Screenshot types
These are the only two page types currently supported :
* #### Details Page
![](https://github.com/dcmc87/ImageHost/blob/master/Screenshot_2017-03-23-22-51-31.png?raw=true)

* #### Gears Page
![](https://github.com/dcmc87/ImageHost/blob/master/Screenshot_2017-04-11-00-37-58.png?raw-true)

## JSON formats
* There are 4 scenarios for any file submitted :
  1. Invalid file type - no JSON response
  2. Failure - not a supported screenshot page type or OCR failed, base64 thumbnail sent back
  3. Success - character detail page or gear page with unique gear name (can identify character), base64 thumbnail and character json sent back
      * if character gear screenshot, tier set to 1, random uniform assigned
  4. Ambiguous/duplicate gear name - same gear name used by multiple characters, may be same or different gear number, base64 thumbnail + character list + gear json sent back

## JSON response structure
```
{  
   "time_taken" : 0  
   "number_total_files" : 3  
  "number_invalid_files" : 1  
  "successful" : [{"<thumbnail_base64_src>" : "<result_json>"},....]  
  "failures" : ["<thumbnail_base64_src>",....]  
  "duplicate_gears" :   
	  [{"thumbnail_base64": "<thumbnail_base64_src>",  
	  "gear_json" : "<gear_json>",  
	  "gear_name" : "<gear_name>",   
	  "char_list" : {"<char_alias>" : <gear_number>,.....}]  
}
```

#### Success
```json

"sharon_rogers":
{
  "defense": {"energy": 0, "physical": 0}, 
  "hp": 0, 
  "critrate": 0.0, 
  "atkspeed": 0.0, 
  "lastUpdate": 0, 
  "gear": [
      [{"val": 0.0, "pref": false, "type": "energy_attack_by_level"}, {"val": 28.0, "pref": false, "type": "all_attack"}, {"val": 57.0, "pref": false, "type": "energy_attack"}, {"val": 80.0, "pref": false, "type": "all_attack"}, {"val": 109.0, "pref": false, "type": "all_attack"}, {"val": 131.0, "pref": false, "type": "all_attack"}, {"val": 172.0, "pref": false, "type": "energy_attack"}, {"val": 210.0, "pref": false, "type": "all_attack"}], 
      [{"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}], 
      [{"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}], 
      [{"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}, {"val": 0.0, "pref": false, "type": ""}]], 
  "uniform": "ca_75", 
  "debuff": 0.0, 
  "ignore_dodge": 0.0, 
  "recorate": 0.0, 
  "skills": [1, 1, 1, 1, 1], 
  "critdamage": 0.0, 
  "attack": {"energy": 0, "physical": 0}, 
  "tier": 1, 
  "dodge": 0.0, 
  "id": "sharon_rogers", 
  "movspeed": 0.0, 
  "uniforms": {}, 
  "scd": 0.0, 
  "defpen": 0.0
}

```
#### Duplicate gear name - only gear json returned
```json
[
{"pref": false, "type": "physical_attack", "val": 45.2}, 
{"pref": false, "type": "physical_attack", "val": 0.0}, 
{"pref": false, "type": "", "val": 60.0}, 
{"pref": false, "type": "physical_attack", "val": 91.0}, 
{"pref": false, "type": "all_attack", "val": 112.0}, 
{"pref": false, "type": "physical_attack", "val": 138.0}, 
{"pref": false, "type": "all_attack", "val": 155.0}, 
{"pref": false, "type": "physical_attack", "val": 213.0}
]
```