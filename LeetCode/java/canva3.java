import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

public class canva3 {
	public static void main(String[] args) {
		System.out.println(fountainActivation(List.of(1, 2, 1)));
	}

	static int fountainActivation(List<Integer> locations) {
		int n = locations.size();
		List<List<Integer>> intervals = new ArrayList<>();
		for (int i = 0; i < locations.size(); i++) {
			int left = Math.max(i+1 - locations.get(i), 1);
			int right = Math.min(i+1 + locations.get(i), n);
			intervals.add(List.of(left, right));
		}

		intervals.sort((a, b) -> a.get(0) - b.get(0));
		System.out.println(intervals);
		// init PriorityQueue
		PriorityQueue<Integer> pq = new PriorityQueue<>();
		for (int i = 0; i < intervals.size(); i++) {
			var cur = intervals.get(i);
			if (pq.isEmpty()) {
				pq.add(cur.get(1));
			} else {
				if (pq.peek() > cur.get(0)) {
					pq.add(cur.get(1));
				} else {
					pq.poll();
					pq.add(cur.get(1));
				}
			}
		}
		return pq.size() - 1;
	}
}
