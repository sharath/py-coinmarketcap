from cmc import WorkerCircularQueue, Worker


class TestWorkerCircularQueue:
    def test_wcq_init(self):
        k = WorkerCircularQueue()
        assert len(k) == 0

    def test_wcq_len(self):
        wq = WorkerCircularQueue()
        for i in range(10):
            wq.add(Worker())
        assert len(wq) == 10

    def test_wcq_next_add(self):
        wq = WorkerCircularQueue()
        for i in range(10):
            wq.add(Worker())

        last = wq.next()
        for _ in range(1000):
            t = wq.next()
            assert len(wq) == 10
            assert last != t
            last = t
