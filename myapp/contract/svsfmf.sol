//SPDX-License-Identifier: MIT
pragma solidity 0.8.19;
contract svsfmf
{
        struct file
    {
        uint id;
        string hash;
    }
    file[] public files;
    string public message;
   function addfile(uint y,string memory m) external{
        files.push(file(y,m));
   }
   function compare(string memory str1,string memory str2) public pure returns(bool)
   {
   if(bytes(str1).length!=bytes(str2).length)
   {
       return false;
   }
   return sha256(abi.encodePacked(str1))==sha256(abi.encodePacked(str2));
   }
   function verify(uint y,string memory m) external
   {
       uint n=files.length;
        for(uint i=0; i<n; i++){
        if(files[i].id==y)
        {
            if(compare(files[i].hash,m)==true)
            {
                
               message="success";
            }
            else
            {
             message="tampered";
               
            }
        }
        else{
        
             message="file not exist";
           
        }
     }

   }
function messagevalue() view public returns(string memory)
{
    return message;
}
}