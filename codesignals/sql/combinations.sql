/*
      So the 'trick' here is to MULTPLY by the ADDITION of logs
      We have a SUM function but not a MULT fuction
      So first find the length then take log of that for each row
      and use sum to add up the logs.  Now exp to reverse it so
      that we have just x*y*z*.....  But it will be a decimal so round it.
*/


CREATE PROCEDURE solution()
BEGIN
	SELECT ROUND(EXP(sum(LOG(LENGTH(characters))))) AS combinations FROM discs;
END