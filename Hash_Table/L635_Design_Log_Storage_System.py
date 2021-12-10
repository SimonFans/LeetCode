Input
["LogSystem", "put", "put", "put", "retrieve", "retrieve"]
[[], [1, "2017:01:01:23:59:59"], [2, "2017:01:01:22:59:59"], [3, "2016:01:01:00:00:00"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"]]
Output
[null, null, null, null, [3, 2, 1], [2, 1]]

Explanation
LogSystem logSystem = new LogSystem();
logSystem.put(1, "2017:01:01:23:59:59");
logSystem.put(2, "2017:01:01:22:59:59");
logSystem.put(3, "2016:01:01:00:00:00");

// return [3,2,1], because you need to return all logs between 2016 and 2017.
logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year");

// return [2,1], because you need to return all logs between Jan. 1, 2016 01:XX:XX and Jan. 1, 2017 23:XX:XX.
// Log 3 is not returned because Jan. 1, 2016 00:00:00 comes before the start of the range.
logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour");


1 <= id <= 500
2000 <= Year <= 2017
1 <= Month <= 12
1 <= Day <= 31
0 <= Hour <= 23
0 <= Minute, Second <= 59
granularity is one of the values ["Year", "Month", "Day", "Hour", "Minute", "Second"].
At most 500 calls will be made to put and retrieve.


class LogSystem:

    def __init__(self):
        self.log = {}

    def put(self, id: int, timestamp: str) -> None:
        self.log[id] = timestamp.split(':')

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        # save log id that meets conditions
        ans = []
        # string to list, remove the ':'
        start_string = start.split(':')
        end_string = end.split(':')
        # Timestamp Mapping : index
        mapping = {'Year': 0, 'Month': 1, 'Day': 2, 'Hour': 3, 'Minute': 4, 'Second': 5}
        # convert start time and end time into an integer
        start_time = int(''.join(start_string[:mapping[granularity]+1]))
        end_time = int(''.join(end_string[:mapping[granularity]+1]))
        # For loop iterate the log dictionary, check if log timestamp >= <= start or end time
        for log_id, log_timestamp in self.log.items():
            curr_log_time = int(''.join(log_timestamp[:mapping[granularity]+1]))
            if curr_log_time >= start_time and curr_log_time <= end_time:
                ans.append(log_id)
        return ans


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)

